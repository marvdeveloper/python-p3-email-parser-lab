import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # Split on commas or whitespace
        email_list = re.split(r'[\s,]+', self.emails.strip())
        
        # Email validation regex pattern (simple but effective for this case)
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Filter only valid emails using regex.match
        valid_emails = [email for email in email_list if re.match(email_pattern, email)]

        # Remove duplicates and sort
        unique_sorted_emails = sorted(set(valid_emails))

        return unique_sorted_emails
