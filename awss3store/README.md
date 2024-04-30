# Amazon S3 (Simple Storage Service) Overview

Amazon S3 (Simple Storage Service) is a scalable object storage service offered by Amazon Web Services (AWS). It is designed to store and retrieve any amount of data from anywhere on the web. S3 provides highly durable and available storage infrastructure, making it suitable for a wide range of use cases, including data backup and archival, content storage and distribution, application data storage, and more.

## Key Concepts

### Buckets

- A bucket is a container for storing objects in S3. All objects are stored within buckets.
- Bucket names must be globally unique across all of AWS.

### Objects

- Objects are the basic entities stored in S3. They consist of data and metadata.
- Each object is identified by a unique key within its bucket.

### Regions

- S3 buckets are stored in a specific AWS region. You can choose the region where your buckets will be stored to optimize latency, minimize costs, or address regulatory requirements.

### Access Control

- S3 provides various mechanisms to control access to buckets and objects, including bucket policies, access control lists (ACLs), and IAM (Identity and Access Management) policies.

### Storage Classes

- S3 offers different storage classes optimized for different access patterns and cost considerations, such as Standard, Intelligent-Tiering, Standard-IA (Infrequent Access), OneZone-IA, Glacier, and others.

### Versioning

- S3 supports object versioning, which allows you to keep multiple versions of an object in the same bucket.

### Lifecycle Policies

- Lifecycle policies enable you to define rules to automatically transition objects to different storage classes or delete them after a specified period.
