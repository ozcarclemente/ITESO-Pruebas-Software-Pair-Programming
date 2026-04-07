
def validate_password(password: str):

    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    if sum(c.isdigit() for c in password) < 2:
        errors.append("The password must contain at least 2 numbers")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one capital letter")

    if not any(not c.isalnum() for c in password):
        errors.append("Password must contain at least one special character")

    if errors:
        return "\n".join(errors)

    return True