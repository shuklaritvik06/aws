import boto3

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='ritvikshuklaqueue',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)

queue_url = sqs.get_queue_url(QueueName='ritvikshuklaqueue')['QueueUrl']
sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Book'
        },
    },
    MessageBody='Hello Bro!'
)

message = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=['All'],
    MaxNumberOfMessages=1,
    MessageAttributeNames=['All'],
    VisibilityTimeout=0,
    WaitTimeSeconds=10
)

print(response['QueueUrl'])
print(sqs.list_queues())
print(message)

if 'Messages' in message:
    receipt_handle = message['Messages'][0]['ReceiptHandle']
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

sqs.delete_queue(QueueUrl=queue_url)
