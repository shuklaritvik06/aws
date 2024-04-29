import boto3

s3 = boto3.client('s3')


def create_bucket(bucket_name_input):
    location = {'LocationConstraint': 'ap-south-1'}
    response = s3.create_bucket(Bucket=bucket_name_input, CreateBucketConfiguration=location)
    print("Bucket created successfully", response)


def upload_file(bucket_name_input, file_path_input, object_key_input):
    s3.upload_file(file_path_input, bucket_name_input, object_key_input)
    print("File uploaded successfully")


def download_file(bucket_name_input, object_key_input, file_path_input):
    s3.download_file(bucket_name_input, object_key_input, file_path_input)
    print("File downloaded successfully")


def list_objects(bucket_name_input):
    response = s3.list_objects_v2(Bucket=bucket_name_input)
    objects = response.get('Contents', [])
    for obj in objects:
        print("Object Key:", obj['Key'])


def delete_object(bucket_name_input, object_key_input):
    response = s3.delete_object(Bucket=bucket_name_input, Key=object_key_input)
    print("Object deleted successfully", response)


def delete_bucket(bucket_name_input):
    response = s3.delete_bucket(Bucket=bucket_name_input)
    print("Bucket deleted successfully", response)


if __name__ == "__main__":
    bucket_name = 'ritvik-shukla-bucket-learning'
    file_path = './example.txt'
    object_key = 'example.txt'
    create_bucket(bucket_name)
    upload_file(bucket_name, file_path, object_key)
    print("Objects in bucket:")
    list_objects(bucket_name)
    download_path = 'downloaded_example.txt'
    download_file(bucket_name, object_key, download_path)
    delete_object(bucket_name, object_key)
    print("Objects in bucket after deletion:")
    list_objects(bucket_name)
    delete_bucket(bucket_name)
