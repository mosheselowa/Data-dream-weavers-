# Class representing an individual email message
class EmailMessage:
    def __init__(self, sender_email, subject, body):
        self.sender_email = sender_email       # Email address of the sender
        self.subject = subject                 # Subject line of the email
        self.body = body                       # Body/content of the email
        self.is_read = False                   # Flag to check if the email has been read

    def mark_as_read(self):
        self.is_read = True                    # Marks the email as read


# List to store email messages
email_inbox = []


# Function to add sample emails to the inbox
def populate_inbox_with_sample_emails():
    sample_email_1 = EmailMessage("Selowa1@gmail.com", "Welcome to the world of Tech", "Great work on the bootcamp")
    sample_email_2 = EmailMessage("Selowa2@gmail.com", "Emergency alert", "Kindly get back to us ASAP")
    sample_email_3 = EmailMessage("Selowa3@gmail.com", "Congratulations on your enrolment", "Please take note of the essential details")

    email_inbox.extend([sample_email_1, sample_email_2, sample_email_3])


# Function to display a list of email subjects
def display_email_subjects():
    for index, email in enumerate(email_inbox):
        print(f"{index}. {email.subject}")


# Function to read and display the full content of a specific email
def read_email_by_index(email_index):
    if 0 <= email_index < len(email_inbox):
        selected_email = email_inbox[email_index]
        print(f"\nFrom: {selected_email.sender_email}")
        print(f"Subject: {selected_email.subject}")
        print(f"\nMessage:\n{selected_email.body}\n")
        selected_email.mark_as_read()
        print(f"The email from {selected_email.sender_email} has been marked as read.\n")
    else:
        print("Invalid email index.\n")


# Function to display only unread emails
def display_unread_emails():
    unread_emails = [email for email in email_inbox if not email.is_read]
    if unread_emails:
        print("\nUnread Emails:")
        for index, email in enumerate(unread_emails):
            print(f"{index}. {email.subject}")
        print()
    else:
        print("\nNo unread emails.\n")


# Populate inbox with sample emails
populate_inbox_with_sample_emails()

# Main application loop
while True:
    user_input = input(
        """\nPlease choose an option:
    1. Read an email
    2. View unread emails
    3. Exit application

Enter your choice: """
    )

    if user_input == "1":
        if not email_inbox:
            print("\nYour inbox is currently empty.\n")
        else:
            print("\nInbox:")
            display_email_subjects()
            try:
                selected_index = int(input("\nEnter the index number of the email you want to read: "))
                read_email_by_index(selected_index)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")

    elif user_input == "2":
        display_unread_emails()

    elif user_input == "3":
        print("\nThank you for using the email application. Goodbye!\n")
        break

    else:
        print("\nInvalid selection. Please enter 1, 2, or 3.\n")
