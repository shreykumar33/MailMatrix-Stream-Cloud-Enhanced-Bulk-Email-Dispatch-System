import boto3
from core.data_manager import load_recipients
from core.template_manager import render_template

# AWS SES configuration
AWS_REGION = 'ap-south-1'  # Change this to your AWS region
SENDER_EMAIL = 'guptashrey555@gmail.com'  # Change this to your verified email address

# AWS credentials (ensure these are stored securely and not hardcoded in production)
AWS_ACCESS_KEY_ID = 'AKIAQ3EGVMMZ5BUZIQP5'  # Replace with your AWS access key ID
AWS_SECRET_ACCESS_KEY = 'kfxuag6VUk+vriwsY6fTSoDTW+7xUkXy6aIKkrVT'  # Replace with your AWS secret access key

# Create an SES client
client = boto3.client(
    'ses',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
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
    # Manually specify the path to the recipients CSV file
    recipients_file = 'C:\\Users\\Welcome\\Downloads\\proj#2-architecture\\data\\recipients.csv'
    
    # Load recipients from CSV
    recipients = load_recipients(recipients_file)
    for recipient in recipients:
        email = recipient['email']
        context = {"name": recipient.get('name', 'Valued Customer')}
        subject = "Welcome to Our Service-working test1"  # Customize subject as needed
        body = render_template("welcome_email.html", context)  # Render email body from template
        response = send_email(email, subject, body)
        print(f"Email sent to {email}! Message ID: {response['MessageId']}")

if __name__ == "__main__":
    main()
