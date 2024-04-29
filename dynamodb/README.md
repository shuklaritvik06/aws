# DynamoDB Overview

**Amazon DynamoDB** is a fully managed NoSQL database service provided by Amazon Web Services (AWS). It's designed to provide seamless scalability, high availability, and low latency for applications requiring consistent, single-digit millisecond response times.

## Key Features

1. **Scalability**:
   - DynamoDB automatically scales to accommodate your workload, with no downtime or performance degradation.

2. **High Availability**:
   - Data is replicated across multiple availability zones to ensure durability and availability even in the event of infrastructure failures.

3. **Performance**:
   - DynamoDB delivers single-digit millisecond response times, making it suitable for applications that require low-latency access to data.

4. **Flexible Data Model**:
   - DynamoDB supports both key-value and document data models, allowing you to store and retrieve data in a format that best suits your application requirements.

5. **Managed Service**:
   - AWS handles all administrative tasks such as hardware provisioning, setup, configuration, replication, software patching, and monitoring, allowing you to focus on building your applications.

## Time and PartiQL Syntax Queries in DynamoDB

## Example

```sql
SELECT * FROM TableName WHERE creationDate > '2024-01-01T00:00:00'
```

## PartiQL Syntax Queries

## Example 1: Basic Query

```sql
SELECT * FROM TableName WHERE partitionKey = 'examplePartitionKey'
```

This query retrieves all items from the `TableName` table where the partition key matches `'examplePartitionKey'`.

### Example 2: Query with Projection

```sql
SELECT attribute1, attribute2 FROM TableName WHERE partitionKey = 'examplePartitionKey'
```

This query retrieves specific attributes (`attribute1` and `attribute2`) from items in the `TableName` table where the partition key matches `'examplePartitionKey'`.

### Example 3: Query with Filter

```sql
SELECT * FROM TableName WHERE partitionKey = 'examplePartitionKey' AND attribute1 > 100
```
