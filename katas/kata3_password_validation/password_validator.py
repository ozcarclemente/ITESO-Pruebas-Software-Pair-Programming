
def validate_password(password: str):

    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    if sum(c.isdigit() for c in password) < 2:
        errors.append("The password must contain at least 2 numbers")

    if errors:
        return "\n".join(errors)

    return True