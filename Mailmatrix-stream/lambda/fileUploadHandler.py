import json
import boto3
import re
from io import StringIO

s3_client = boto3.client('s3')
ses_client = boto3.client('ses', region_name='ap-south-1')

# Basic email validation function
def is_valid_email(email):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email)

def render_template(template_content, context):
    # Use the template as a string and replace the placeholders with actual data
    for key, value in context.items():
        template_content = template_content.replace('{{ ' + key + ' }}', value)
    return template_content

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get the recipients file from S3
    response = s3_client.get_object(Bucket=bucket, Key=key)
    recipients_data = response['Body'].read().decode('utf-8')

    # Read and process CSV data
    recipients = recipients_data.strip().split("\n")
    
    # Get the welcome email template from S3
    template_response = s3_client.get_object(Bucket=bucket, Key='welcome_email.html')
    welcome_template = template_response['Body'].read().decode('utf-8')

    # Iterate through each recipient
    for recipient_line in recipients:
        recipient_info = recipient_line.split(",")  # Assuming CSV format: email,name
        email = recipient_info[0].strip()  # Make sure to strip any extra spaces
        name = recipient_info[1].strip() if len(recipient_info) > 1 else 'Valued Customer'
        
        # Validate email before attempting to send
        if not is_valid_email(email):
            print(f"Invalid email address: {email}")
            continue  # Skip sending email if invalid

        # Render the template with dynamic content
        email_body = render_template(welcome_template, {'name': name})

        # Send the email via SES
        try:
            ses_client.send_email(
                Source='guptashrey555@gmail.com',
                Destination={'ToAddresses': [email]},
                Message={
                    'Subject': {'Data': "Welcome to Mail-Matrix: Stream!"},
                    'Body': {'Html': {'Data': email_body}}
                }
            )
            print(f"Email sent successfully to {email}")
        except Exception as e:
            print(f"Error sending email to {email}: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Emails processed successfully!')
    }
