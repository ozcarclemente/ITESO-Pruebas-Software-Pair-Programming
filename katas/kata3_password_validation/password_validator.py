
def validate_password(password: str):

    if len(password) < 8:
        return "Password must be at least 8 characters long"
    
    if sum(c.isdigit() for c in password) < 2:
        return "The password must contain at least 2 numbers"
    
    return True