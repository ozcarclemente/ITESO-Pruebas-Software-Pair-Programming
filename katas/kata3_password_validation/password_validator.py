
def validate_password(password: str):

    if len(password) < 8:
        return "Password must be at least 8 characters long"
    
    return True