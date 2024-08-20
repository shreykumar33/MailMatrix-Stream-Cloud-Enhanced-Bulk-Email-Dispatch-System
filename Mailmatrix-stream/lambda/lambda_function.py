import json
import boto3
import csv
import io

# Initialize clients
s3 = boto3.client('s3')
ses = boto3.client('ses')

def lambda_handler(event, context):
    # Extract bucket name and file key from the event
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        event_name = event['Records'][0]['eventName']
    except KeyError as e:
        print(f"Error extracting event data: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps('Error extracting event data.')
        }
    
    # Define recipients list
    recipients = []

    try:
        # Fetch the CSV file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        csv_content = response['Body'].read().decode('utf-8')
        
        # Debug logging: print CSV content
        print("CSV Content:", csv_content)
        
        # Parse CSV
        reader = csv.DictReader(io.StringIO(csv_content))
        
        # Collect email addresses from CSV
        for row in reader:
            try:
                # Debug logging: print row content
                print("Row Data:", row)
                
                recipient = row['email']  # Updated to match CSV field name
                recipients.append(recipient)
            except KeyError as e:
                print(f"Error: Missing required field in CSV: {e}")
    
    except Exception as e:
        print(f"Error processing S3 object: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing S3 object.')
        }
    
    if "PutObject" in event_name:
        # Handle object creation event
        print(f"Handling object creation event for bucket {bucket_name} with key {file_key}")
        
        subject = "The service is live!"
        body = "Welcome to our service!"
        
        # Send emails to recipients listed in CSV
        for recipient in recipients:
            try:
                response = ses.send_email(
                    Source='guptashrey555@gmail.com',
                    Destination={
                        'ToAddresses': [recipient]
                    },
                    Message={
                        'Subject': {
                            'Data': subject
                        },
                        'Body': {
                            'Text': {
                                'Data': body
                            }
                        }
                    }
                )
                print(f"Email sent to {recipient}! Message ID: {response['MessageId']}")
            
            except Exception as e:
                print(f"Error sending email to {recipient}: {str(e)}")
    
    elif "DeleteObject" in event_name:
        # Handle object deletion event
        print(f"Handling object deletion event for bucket {bucket_name} with key {file_key}")
        subject = "You have been removed from the service"
        body = f"The object with key {file_key} has been deleted from bucket {bucket_name}. You have been removed from the service."
        
        # Send deletion notification to all recipients
        for recipient in recipients:
            try:
                response = ses.send_email(
                    Source='guptashrey555@gmail.com',
                    Destination={
                        'ToAddresses': [recipient]
                    },
                    Message={
                        'Subject': {
                            'Data': subject
                        },
                        'Body': {
                            'Text': {
                                'Data': body
                            }
                        }
                    }
                )
                print(f"Deletion notification sent to {recipient}! Message ID: {response['MessageId']}")
            
            except Exception as e:
                print(f"Error sending deletion notification to {recipient}: {str(e)}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processed S3 event successfully!')
    }
