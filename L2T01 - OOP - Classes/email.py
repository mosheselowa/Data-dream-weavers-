class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True


inbox = []


def populate_inbox():
    email1 = Email("Selowa1@gmail.com", "Welcome to the world of Tech", "Great work on the bootcamp")
    email2 = Email("Selowa2@gmail.com", "Emergency alert", "Kindly get back to us ASAP")
    email3 = Email("Selowa3@gmail.com", "Congratulations on your enrolment", "Please take note of the essential details")

    inbox.extend([email1, email2, email3])


def list_emails():
    for index, email in enumerate(inbox):
        print(f"{index}. {email.subject_line}")


def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nEmail from: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"\nContent:\n{email.email_content}\n")
        email.mark_as_read()
        print(f"The email from {email.email_address} has been marked as read.\n")
    else:
        print("Invalid email index.\n")


def view_unread_emails():
    unread_emails = [email for email in inbox if not email.has_been_read]
    if unread_emails:
        print("\nUnread Emails:")
        for index, email in enumerate(unread_emails):
            print(f"{index}. {email.subject_line}")
        print()
    else:
        print("\nNo unread emails.\n")


# Populate the inbox with sample emails
populate_inbox()

# Main program loop
while True:
    user_choice = input(
        """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

Enter selection: """
    )

    if user_choice == "1":
        if not inbox:
            print("\nInbox is empty.\n")
        else:
            print("\nList of Emails:")
            list_emails()
            try:
                email_index = int(input("\nEnter the index of the email you want to read: "))
                read_email(email_index)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")

    elif user_choice == "2":
        view_unread_emails()

    elif user_choice == "3":
        print("\nGoodbye!")
        break

    else:
        print("\nOops - incorrect input. Please enter 1, 2, or 3.\n")