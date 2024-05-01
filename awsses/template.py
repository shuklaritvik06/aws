import boto3

ses = boto3.client('ses')

response2 = ses.create_template(
    Template={
        'TemplateName': 'BASIC_TEMPLATE2',
        'SubjectPart': 'My Email Subject',
        'TextPart': 'Hello Bro I am textual Content!',
        'HtmlPart': '<h1>Hi {{REPLACEMENT_TAG_NAME}}</h1>'
    }
)

ses.verify_email_identity(
    EmailAddress='hello@ritvikshukla.xyz'
)

ses.verify_email_identity(
    EmailAddress='ritvikshukla261@gmail.com'
)

ses.verify_email_identity(
    EmailAddress='ankitjhanjhari0@gmail.com'
)

email_response = ses.send_templated_email(
  Source='hello@ritvikshukla.xyz',
  Destination={
    'ToAddresses': [
      'ankitjhanjhari0@gmail.com',
    ],
  },
  ReplyToAddresses=[
    'hello@ritvikshukla.xyz',
  ],
  Template='BASIC_TEMPLATE2',
  TemplateData='{ \"REPLACEMENT_TAG_NAME\":\"REPLACEMENT_VALUE\" }'
)

print(email_response)


