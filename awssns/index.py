import boto3

sns = boto3.client('sns')

response = sns.create_topic(Name='MyTopic')

topic_arn = response['TopicArn']
print("Created topic ARN:", topic_arn)

print("Published message ID:", response['MessageId'])

response = sns.list_topics()
print("Existing topics:", response['Topics'])

response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='ritvikshukla261@gmail.com'
)

print("Subscription ARN:", response['SubscriptionArn'])


response = sns.publish(
    TopicArn=topic_arn,
    Message='Hello, world!',
    Subject='Test message'
)

sns.delete_topic(TopicArn=topic_arn)
