import boto3

ses = boto3.client('ses')

response = ses.verify_email_identity(
    EmailAddress='hello@ritvikshukla.xyz'
)

response2 = ses.verify_domain_identity(
    Domain='ritvikshukla.xyz'
)

response3 = ses.list_identities(
    IdentityType='EmailAddress',
    MaxItems=10
)

response4 = ses.list_identities(
    IdentityType='EmailAddress',
    MaxItems=10
)

response5 = ses.delete_identity(
    Identity='hello@ritvikshukla.xyz'
)

print(response)
print(response2)
print(response3)
