# AWS SNS (Simple Notification Service)

## Overview

AWS Simple Notification Service (SNS) is a fully managed messaging service provided by Amazon Web Services (AWS) that enables you to send notifications from the cloud to various endpoints such as email, SMS, HTTP/S, or even to other AWS services such as SQS, Lambda, or mobile push notifications.

## Features

- **Pub/Sub Messaging**: SNS follows a publish-subscribe (pub/sub) model, allowing you to publish messages to topics, which are then delivered to subscribers.
  
- **Multiple Endpoints**: Supports various endpoint types including email, SMS, HTTP/S, SQS, Lambda, mobile push notifications (iOS, Android), and more.
  
- **Message Filtering**: SNS supports message filtering policies, allowing subscribers to receive only the messages they are interested in.
  
- **Cross-Region Replication**: SNS topics can be replicated across different AWS regions for improved availability and durability.
  
- **Message Encryption**: Messages sent through SNS can be encrypted using AWS Key Management Service (KMS) for enhanced security.
