if __name__ == "__main__":
    recipients = load_recipients("data/recipients.csv")
    validate_recipients(recipients)
    print("All recipients are valid.")
