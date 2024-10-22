# MailMatrix: Bulk Email Notification System Using AWS Services

## Overview

MailMatrix is an automated bulk email notification system built with AWS serverless services. It allows users to upload CSV files containing recipient data, personalize email content, and dispatch bulk emails using Amazon SES. The system leverages AWS Lambda for processing, Amazon S3 for file storage, and monitoring and security services like CloudWatch and IAM to ensure seamless and secure operations. The architecture is designed to be fully scalable, cost-efficient, and customizable for real-world bulk mailing scenarios.

## Purpose and Motivation

Sending bulk emails efficiently and securely can be challenging, especially when managing large recipient lists, dynamic content personalization, and real-time monitoring of delivery status. MailMatrix addresses these challenges by utilizing AWS's serverless infrastructure to build a highly available, event-driven email notification system.

With MailMatrix:
- **No infrastructure management**: AWS Lambda and other services handle scaling automatically.
- **Personalized email content**: Each recipient receives personalized emails based on CSV data, ensuring relevant communication.
- **End-to-end security**: Data encryption, access control, and auditing are built into the workflow.
- **Monitoring and Alerts**: Real-time monitoring and alerts keep track of the status and any issues.

## Architecture

MailMatrix follows a serverless architecture using the following AWS services:

![project2 architecture](https://github.com/user-attachments/assets/34eecd37-2a16-49bc-a79b-43de87b1add5)


1. **Amazon S3**: CSV files containing recipient details (e.g., name, email) are uploaded here, triggering events.
2. **Amazon EventBridge**: Listens for S3 events and triggers the Lambda function for processing.
3. **AWS Lambda**: Handles business logic: from parsing CSV files, personalizing email templates, and sending them via SES.
4. **Amazon SES (Simple Email Service)**: Sends personalized emails to the recipients based on the data and templates processed by Lambda.
5. **Amazon CloudWatch**: Monitors Lambda performance, tracks logs, and raises alarms in case of failures.
6. **Amazon SNS (Simple Notification Service)**: Sends notifications via email or SMS when errors occur during processing.
7. **AWS IAM**: Manages permissions and security policies for Lambda to interact with S3, SES, and CloudWatch.

## Project Workflow

![workflow](https://github.com/user-attachments/assets/b1ea7e1a-cf1b-4082-8bee-33ca819318a0)


1. **Upload CSV File**: A CSV file with recipient information (e.g., name, email) is uploaded to an Amazon S3 bucket.
2. **Event Trigger**: An S3 event triggers Amazon EventBridge, which in turn activates the AWS Lambda function.
3. **Data Processing**: Lambda processes the CSV file, validates the data, personalizes the email templates (using tools like Jinja2), and prepares them for dispatch.
4. **Email Dispatch**: Lambda sends the personalized emails using Amazon SES.
5. **Monitoring and Alerts**: CloudWatch monitors the Lambda function. If there’s an error, SNS sends an alert to the user via email or SMS.
6. **Security**: Data is encrypted at rest in S3 and in transit. IAM ensures proper role-based access control.

## How to Use

### Prerequisites
- AWS Account with permissions for SES, S3, Lambda, IAM, CloudWatch, SNS, and EventBridge.
- Familiarity with Python, AWS CLI, and basic knowledge of AWS services.
- Domain verified in SES for sending emails.

### Step-by-Step Setup

1. **Configure AWS CLI**: Ensure you have the AWS CLI installed and configured with your credentials.
2. **Create the S3 Bucket**: Create an S3 bucket where you will upload your CSV files containing recipient details.

   
 ![buck1](https://github.com/user-attachments/assets/bdaa6f84-115f-48ea-a7a2-d8cfc9443f7b)

 ![buck2](https://github.com/user-attachments/assets/4cc846dc-3629-481f-9cc3-f82b1b5e0810)

 ![buck3](https://github.com/user-attachments/assets/91600141-3160-4715-a7dc-79bc0fe30a91)

   
3. **Set Up SES**: Verify your domain in Amazon SES and configure SES to send emails from your verified domain.

   ![ses](https://github.com/user-attachments/assets/8a4c39f6-4d96-4ddc-a1d1-fc47df3496e2)


4. **Deploy Lambda Function**: Upload your Lambda function code (Python) via the AWS Lambda console or CLI. Set up an S3 event trigger via EventBridge to invoke Lambda when a new file is uploaded.
   ![lambda1](https://github.com/user-attachments/assets/2cd36c45-dbbe-4010-af5b-411776b90727)
   ![lambda2](https://github.com/user-attachments/assets/e885b1c1-ef5c-4c0b-85ca-343c8ba51492)
   ![lambda3](https://github.com/user-attachments/assets/6e644405-1c5c-46e9-aa98-70db4f854fe5)
   ![lambda4](https://github.com/user-attachments/assets/fe507a18-e6f6-4481-94c1-3342753ae6db)

5. **Configure CloudWatch and SNS**: Set up CloudWatch alarms to monitor Lambda's performance. Create an SNS topic to send notifications in case of errors.

   ![cloudformation](https://github.com/user-attachments/assets/7a7536be-4955-45d6-b804-106526394c80)

   ![cloudwatch](https://github.com/user-attachments/assets/d66d0dc3-bd2c-40dc-84c1-d5bb300addfe)

   ![cloudwatch1](https://github.com/user-attachments/assets/e7725345-5dcd-4c19-8b19-c0e74180fab5)

   ![cloudwatch3](https://github.com/user-attachments/assets/bbe47557-d426-4cdf-8863-6913e582680a)

   ![cloudwatchtest](https://github.com/user-attachments/assets/100e2daf-8ed0-4663-98aa-3c47f5a9f9ce)
   #alarms deployment --

6. **IAM Roles and Permissions**: Assign a well-defined IAM role to your Lambda function with least-privilege permissions to access S3, SES, and CloudWatch.
    
    ![role 1](https://github.com/user-attachments/assets/f4935ab3-e5c9-4469-8da4-a959b237668e)

    ![role 2 custom](https://github.com/user-attachments/assets/61b7a043-4342-4537-8c3d-126607115785)

    ![roles 3 custom](https://github.com/user-attachments/assets/3cc51a23-3190-4795-bef2-c7abb9255783)

    ![trigger_role](https://github.com/user-attachments/assets/c3f12be6-c8d4-4b2a-94a4-9a56051ca975)

7. **Test the System**: Upload a CSV file to the S3 bucket and verify that emails are sent to the recipients listed in the file. Monitor CloudWatch logs and ensure that any errors trigger alerts via SNS.

    ![sns1](https://github.com/user-attachments/assets/fef2afba-8c64-4bc0-b6a4-d4d172029cf6)

    ![sns2](https://github.com/user-attachments/assets/56659b5b-9c68-4fb5-96bf-74ba21abe9e6)

    ![mail2](https://github.com/user-attachments/assets/fca7a716-5394-434e-8dd7-151466c72a55)

    ![mail3](https://github.com/user-attachments/assets/427d068a-ec3f-4ce7-8a37-b7e54f7122f7)


## Notes and Best Practices

1. **Never Hardcode AWS Credentials**: Use IAM roles and AWS environment variables for handling credentials. Hardcoding credentials in code is a security risk.
2. **Input Validation**: Always validate the data being uploaded, including checking the CSV structure and sanitizing input data to avoid vulnerabilities.
3. **Use IAM Roles with Least Privilege**: Assign only the necessary permissions to Lambda using IAM roles. Avoid granting broader permissions than required.
4. **Monitor Costs**: Since SES and Lambda are pay-per-use services, monitor usage to avoid unexpected billing spikes. Use AWS Budgets to set alerts.
5. **Email Limits in SES**: Ensure that your account has sufficient SES sending limits to handle the volume of emails. Start with verified emails in a sandbox environment.
6. **Error Handling**: Implement robust error handling within your Lambda function to gracefully manage failed email sends or unexpected data formats.
7. **Logging and Monitoring**: Regularly check CloudWatch logs for troubleshooting and ensure smooth operations. Set alarms for critical issues.

## Potential Enhancements

To scale the MailMatrix project beyond its current sandbox environment, one can easily transition to sending emails to unverified recipients by moving out of the SES sandbox. This transition involves a simple process of requesting production access through the Amazon SES console. Once your SES account is out of the sandbox, it can send emails to any email addresses, not just those that are verified. This scalability ensures that MailMatrix can handle large-scale email campaigns efficiently, reaching a broader audience while maintaining the same level of automation, security, and monitoring. By expanding the SES sending limits and integrating with additional AWS services or third-party tools - further enhance the system's capacity and functionality to meet growing demands.

***

## Use Case(#01): Automated Bulk Sending of Offer and Rejection Letters with PDF Attachments

This use case demonstrates how `mailmatrix-stream` can be customized to automatically send offer and rejection letters to candidates via email, with PDF attachments. The list of candidates, their emails, and corresponding letters are provided in a `recipient.csv` file, and the Lambda function handles the rest.

### Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Folder Structure](#folder-structure)
- [Setup and Configuration](#setup-and-configuration)
  - [Step 1: Prepare the Recipient List](#step-1-prepare-the-recipient-list)
  - [Step 2: Customize the Lambda Function](#step-2-customize-the-lambda-function)
  - [Step 3: AWS Resource Configuration](#step-3-aws-resource-configuration)
- [Testing](#testing)
- [Conclusion](#conclusion)

## Introduction

This customization extends the functionality of `mailmatrix-stream` to allow HR teams or organizations to send bulk offer and rejection letters to candidates. By uploading a recipient list in CSV format and providing the corresponding PDF documents, the Lambda function will send the appropriate email with the attached letter to each recipient.

## Prerequisites

- **AWS Lambda**: Function for sending bulk emails.
- **AWS SES (Simple Email Service)**: Service used to send emails.
- **Recipient List CSV**: A file containing recipient emails, names, statuses (Offer/Rejection), and corresponding PDFs.
- **PDF Offer and Rejection Letters**: Individualized PDFs for each candidate stored locally or in an S3 bucket.

## Folder Structure

This use case demonstrates how the `mailmatrix-stream` system can be extended to send bulk offer and rejection letters to candidates, complete with PDF attachments, using AWS Lambda and SES.

### Directory Structure

```bash
use_case/
├── bulk_offer_rejection/
│   ├── recipient.csv                  # List of email recipients with offer/rejection status and corresponding attachment file names
│   ├── offer_letter_template.pdf       # Template for the offer letter to be sent as a PDF attachment
│   ├── rejection_letter_template.pdf   # Template for the rejection letter to be sent as a PDF attachment
│   ├── lambda_function.py              # Lambda function code for sending bulk emails with attachments
│   ├── README.md                       # Documentation for the bulk offer/rejection use case
│   └── requirements.txt                # Python dependencies for the Lambda function
```


### `recipient.csv` Format

| Email              | Name           | Status    | Attachment_File            |
|--------------------|----------------|-----------|----------------------------|
| shrey@example.com   | Shrey Kumar    | Offer     | offer_shrey_kumar.pdf      |
| shreya@example.com  | Shreya Mehta   | Rejection | rejection_shreya_mehta.pdf |
| ramesh@example.com  | Ramesh Verma   | Offer     | offer_ramesh_verma.pdf     |

The CSV file should contain the following columns:
- **Email**: Candidate's email address.
- **Name**: Candidate's name.
- **Status**: Status of the candidate (Offer or Rejection).
- **Attachment_File**: The file name of the PDF that will be attached to the email.

## Setup and Configuration

### Step 1: Prepare the Recipient List

Prepare the `recipient.csv` file with the relevant details (email, name, status, and attachment file) as outlined above. Ensure that the attachment filenames in the CSV match the actual filenames of the PDFs stored locally or in an S3 bucket.

### Step 2: Customize the Lambda Function

We customize the `lambda_function.py` to process the `recipient.csv` and send emails with the appropriate PDF attachments based on the candidate's status (Offer or Rejection).

#### Key Customizations in `lambda_function.py`

- **CSV Parsing**: Reads the recipient list from `recipient.csv`.
- **Conditional Logic**: Determines whether to send an offer or rejection letter based on the `Status` column.
- **PDF Attachment**: Fetches the corresponding PDF file from local storage or an S3 bucket and attaches it to the email.
- **Email Sending**: Sends the email through AWS SES with the correct subject line and attached PDF.

#### Illustrative Code for implementing Lambda function 

```python
import boto3
import csv
import os


ses_client = boto3.client('ses', region_name='ap-south-1')

def send_email(recipient, subject, body_text, body_html, attachment):
    # Email sending logic with attachment
    pass

def lambda_handler(event, context):
    
    with open('/path/to/recipient.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            email = row['Email']
            name = row['Name']
            status = row['Status']
            attachment_file = row['Attachment_File']

            if status == 'Offer':
                subject = f"Offer Letter for {name}"
                body_text = f"Dear {name},\n\nPlease find your offer letter attached."
            else:
                subject = f"Rejection Letter for {name}"
                body_text = f"Dear {name},\n\nWe regret to inform you that you have not been selected."

            # Load attachment from local path or S3
            with open(f'/path/to/attachments/{attachment_file}', 'rb') as pdf_file:
                pdf_data = pdf_file.read()

            send_email(email, subject, body_text, None, pdf_data)

```
### Step 3: AWS Resource Configuration
-  **SES Setup**: Verify the sending email address (e.g., My own: guptashrey555@gmail.com) in SES.
-  **S3 Bucket (optional)**: Store the PDF files for offer and rejection letters if accessing remotely.
-  **Lambda Deployment**: Deploy the Lambda function via the AWS Management Console. Ensure it has necessary permissions for SES and S3 (if using S3 for PDFs).
## Testing
Test the Lambda function by running it on smaller batches of recipients from the recipient.csv file:

- **Validation**: Verify that emails are sent correctly to each recipient.
- **Attachment Check**: Ensure that the correct offer or rejection letter PDF is attached to each email.
- **SES Sending Limits**: Confirm that you are within SES sending limits and that emails are not flagged as spam.
## Conclusion
This use case provides a streamlined solution for automating the bulk sending of offer and rejection letters with PDF attachments. By using the power of AWS Lambda, SES, and simple data management in CSV files, HR teams can efficiently communicate with large groups of candidates with minimal manual effort.

With 'mailmatrix-stream', the customization demonstrates how to handle bulk communications securely, quickly, and with complete automation.

***
<img width="1138" alt="Screenshot 2024-10-22 at 5 19 07 PM" src="https://github.com/user-attachments/assets/4e12c6c8-2d27-4c34-8d6c-7dd14986278d">
<img width="1502" alt="Screenshot 2024-10-22 at 5 27 06 PM" src="https://github.com/user-attachments/assets/56a9cb83-7ab9-4c05-81f4-c5950bfbcd0f">


- **Multiple Templates**: Extend the system to support multiple templates, allowing dynamic content for different recipients or campaigns.
- **Database Integration**: Add a database (e.g., DynamoDB) to track email sending history, store recipient preferences, and handle analytics.
- **Custom Reporting**: Enhance reporting capabilities to track open rates, bounce rates, and email deliverability.
- **Retry Mechanism**: Implement an automatic retry mechanism for failed emails to ensure delivery.

## Conclusion

MailMatrix provides an efficient, secure, and scalable solution for sending bulk personalized emails using AWS serverless architecture. The project adheres to AWS best practices for security, monitoring, and performance while remaining highly customizable and easy to deploy.

## Tips and Notes
- Verify SES domains and emails before production use.
- Keep track of SES sending quotas to avoid exceeding limits.
- Use CloudWatch logs and dashboards for performance tuning and troubleshooting.
- Ensure S3 buckets are secure by enabling server-side encryption and limiting access via bucket policies.

[![GitHub](https://img.shields.io/badge/GitHub-shreykumar33-B22222?style=flat-square&logo=github)](https://github.com/shreykumar33)
