def verify_username(username):
    if not username[0].isalpha():
        return False

    for char in username:
        if not (
            char.isalpha() or
            char.isdigit() or
            char == '-' or
            char == '_'
        ):
            return False

    return True


def verify_website(website):
    for char in website:
        if not (
            char.isalpha() or
            char.isdigit()
        ):
            return False

    return True


def verify_extension(extension):
    if len(extension) > 3:
        return False

    for char in extension:
        if not char.isalpha():
            return False

    return True


def verify_email(email):
    if not email:
        raise ValueError('Invalid email')

    username, final_part = email.split('@')
    website, extension = final_part.split('.')

    if not verify_username(username):
        raise ValueError('Invalid username')

    if not verify_website(website):
        raise ValueError('Invalid website')

    if not verify_extension(extension):
        raise ValueError('Invalid extension')

    return 'Valid email'
