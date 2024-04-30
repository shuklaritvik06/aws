import base64
import logging

import boto3
from botocore.exceptions import ClientError
from cryptography.fernet import Fernet


def encrypt_file(filename, cmk_id):
    try:
        with open(filename, 'rb') as file:
            file_contents = file.read()
    except IOError as e:
        logging.error(e)
        return False
    data_key_encrypted, data_key_plaintext = create_data_key(cmk_id)
    if data_key_encrypted is None:
        return False
    logging.info('Created new AWS KMS data key')
    f = Fernet(data_key_plaintext)
    file_contents_encrypted = f.encrypt(file_contents)
    try:
        with open(filename + '.encrypted', 'wb') as file_encrypted:
            file_encrypted.write(len(data_key_encrypted).to_bytes(2, byteorder='big'))
            file_encrypted.write(data_key_encrypted)
            file_encrypted.write(file_contents_encrypted)
    except IOError as e:
        logging.error(e)
        return False
    return True


def retrieve_cmk(desc):
    kms_client = boto3.client('kms')
    try:
        response = kms_client.list_keys()
    except ClientError as e:
        logging.error(e)
        return None, None
    done = False
    while not done:
        for cmk in response['Keys']:
            try:
                key_info = kms_client.describe_key(KeyId=cmk['KeyArn'])
            except ClientError as e:
                logging.error(e)
                return None, None
            if key_info['KeyMetadata']['Description'] == desc:
                return cmk['KeyId'], cmk['KeyArn']
        if not response['Truncated']:
            logging.debug('A CMK with the specified description was not found')
            done = True
        else:
            try:
                response = kms_client.list_keys(Marker=response['NextMarker'])
            except ClientError as e:
                logging.error(e)
                return None, None
    return None, None


def create_cmk(desc='Customer Master Key'):
    kms_client = boto3.client('kms')
    try:
        response = kms_client.create_key(Description=desc)
    except ClientError as e:
        logging.error(e)
        return None, None
    return response['KeyMetadata']['KeyId'], response['KeyMetadata']['Arn']


def create_data_key(cmk_id, key_spec='AES_256'):
    kms_client = boto3.client('kms')
    try:
        response = kms_client.generate_data_key(KeyId=cmk_id, KeySpec=key_spec)
    except ClientError as e:
        logging.error(e)
        return None, None

    return response['CiphertextBlob'], base64.b64encode(response['Plaintext'])


def decrypt_data_key(data_key_encrypted):
    kms_client = boto3.client('kms')
    try:
        response = kms_client.decrypt(CiphertextBlob=data_key_encrypted)
    except ClientError as e:
        logging.error(e)
        return None

    return base64.b64encode((response['Plaintext']))


def decrypt_data(filename):
    try:
        with open(filename, 'rb') as file:
            file_contents = file.read()
    except IOError as e:
        logging.error(e)
        return False
    data_key_encrypted_len = int.from_bytes(file_contents[:2], byteorder='big') + 2
    data_key_encrypted = file_contents[2:data_key_encrypted_len]
    data_key_plaintext = decrypt_data_key(data_key_encrypted)
    if data_key_plaintext is None:
        return False
    f = Fernet(data_key_plaintext)
    file_contents_decrypted = f.decrypt(file_contents[data_key_encrypted_len:])
    try:
        with open(filename + '.decrypted', 'wb') as file_decrypted:
            file_decrypted.write(file_contents_decrypted)
    except IOError as e:
        logging.error(e)
        return False
    return True


print(create_cmk())
print(retrieve_cmk(desc='Customer Master Key'))
print(create_data_key('82b74a88-048a-49cb-8fc3-62de9ec05b37'))
print(encrypt_file('./example.txt', '82b74a88-048a-49cb-8fc3-62de9ec05b37'))
print(decrypt_data('./example.txt.encrypted'))
