import argparse
import os
from core.data_manager import load_recipients
from core.template_manager import render_template
from email_sender import send_email 

def main():
    # Parsing command line arguments
    parser = argparse.ArgumentParser(description='CLI tool for sending emails.')
    parser.add_argument('--recipients', required=True, help='Path to recipients CSV file')
    parser.add_argument('--template', required=True, help='Path to email template file')
    parser.add_argument('--subject', required=True, help='Email subject')
    args = parser.parse_args()

    # Load recipients
    recipients_file = args.recipients
    template_file = os.path.basename(args.template)  #the template file name only
    subject = args.subject

    
    recipients = load_recipients(recipients_file)

    # Render the email body for each recipient and send the email
    for recipient in recipients:
        email = recipient['email']
        context = {"name": recipient.get('name', 'Valued Customer')}
        body = render_template(template_file, context) 
        response = send_email(email, subject, body)
        print(f"Email sent to {email}! Message ID: {response['MessageId']}")

if __name__ == "__main__":
    main()
