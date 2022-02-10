from exercise_three import verify_email


def valid_emails(email_list):
    result = []

    for email in email_list:
        try:
            if verify_email(email) == 'Valid email':
                result.append(email)
        except ValueError:
            print('An email was invalid')

    return result
