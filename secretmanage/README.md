# AWS Secrets Manager Overview

AWS Secrets Manager is a service provided by Amazon Web Services (AWS) that helps you securely store, manage, and retrieve sensitive information such as API keys, passwords, and database credentials. It enables you to centralize the management of secrets and provides robust access control and auditing capabilities.

## Key Concepts

### Secrets

- A secret is any piece of sensitive information that needs to be securely stored and managed. This can include database credentials, API keys, encryption keys, and other types of sensitive data.

### Secrets Manager

- AWS Secrets Manager is the service provided by AWS for storing and managing secrets.
- Secrets Manager offers features such as automatic rotation of credentials, fine-grained access control using IAM policies, integration with AWS services and SDKs, and audit logging.

### Rotation

- Secret rotation is the process of regularly updating and replacing secret values to enhance security.
- Secrets Manager provides built-in support for automatic rotation of credentials for supported services such as RDS databases, Redshift clusters, and more.

### Versioning

- Secrets Manager supports versioning of secrets, allowing you to store multiple versions of a secret and retrieve specific versions as needed.

### Access Control

- Access to secrets in Secrets Manager is controlled using IAM (Identity and Access Management) policies.
- IAM policies define who can access which secrets and what actions they can perform on those secrets.

### Integration

- Secrets Manager seamlessly integrates with other AWS services such as Amazon RDS, Amazon Redshift, AWS Lambda, and AWS CloudFormation, enabling you to securely retrieve secrets within your applications and infrastructure.
