#Smart Contact Manager
def organize_contacts(contact_list):
    # 1. Create helper functions for validation

    # Function to validate email format
    def is_valid_email(email):
        return '@' in email and '.' in email and ' ' not in email

    # Function to clean and validate phone numbers
    def clean_phone(phone):
        digits = ''.join(filter(str.isdigit, phone))
        return digits if len(digits) == 10 else None

    # 2. Process each contact
    cleaned_contacts = []
    seen_emails = set()
    seen_phones = set()

    for contact in contact_list:
        # Clean email (lowercase) and phone (digits only)
        cleaned_email = contact['email'].lower()
        cleaned_phone = clean_phone(contact['phone'])

        # Check if email and phone are valid
        if not is_valid_email(cleaned_email) or cleaned_phone is None:
            continue

        # Check for duplicates
        if cleaned_email in seen_emails or cleaned_phone in seen_phones:
            continue

        seen_emails.add(cleaned_email)
        seen_phones.add(cleaned_phone)
        cleaned_contacts.append({
            'name': contact['name'],
            'email': cleaned_email,
            'phone': cleaned_phone
        })

    # 3. Return the clean contact list
    return cleaned_contacts
contacts = [
    {"name": "John Doe", "email": "john@email.com", "phone": "123-456-7890"}
]
print(organize_contacts(contacts))