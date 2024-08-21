import csv
import os

def load_recipients(file_path):
    #getting path to the CSV file
    file_path = os.path.abspath(file_path)
    
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        recipients = [row for row in reader]
    return recipients

def validate_recipients(recipients):
    for recipient in recipients:
        if not recipient['email']:
            raise ValueError("Email is required")
    return True

if __name__ == "__main__":
    getting the directory of this script
    script_dir = os.path.dirname(__file__)
    
    #Construct path to the CSV file
    recipients_file = os.path.join(script_dir, '..', '..', 'data', 'recipients.csv')
    
    recipients = load_recipients(recipients_file)
    validate_recipients(recipients)
    print("All recipients are valid.")
#locally this was working setup for managing data in my recipient data csv