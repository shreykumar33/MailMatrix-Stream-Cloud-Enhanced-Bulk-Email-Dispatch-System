import boto3
import os
from core.data_manager import load_recipients
from core.template_manager import render_template

AWS_REGION = os.getenv('AWS_REGION', 'ap-south-1')
SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'a_verified_email@example.com')

client = boto3.client(
    'ses',
    region_name=AWS_REGION
)

def send_email(recipient_email, subject, body):
    response = client.send_email(
        Source=SENDER_EMAIL,
        Destination={
            'ToAddresses': [recipient_email]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Html': {
                    'Data': body
                }
            }
        }
    )
    return response

def main():
    recipients_file = os.getenv('RECIPIENTS_FILE_PATH', 'data/recipients.csv')
    recipients = load_recipients(recipients_file)
    for recipient in recipients:
        email = recipient['email']
        context = {"name": recipient.get('name', 'Valued Customer')}
        subject = "Welcome to Our Service-working test1"
        body = render_template("welcome_email.html", context)
        response = send_email(email, subject, body)
        print(f"Email sent to {email}! Message ID: {response['MessageId']}")

if __name__ == "__main__":
    main()
