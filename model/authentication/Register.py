import bcrypt
from password_strength import PasswordPolicy
from email_validator import validate_email, EmailNotValidError

def validateEmail(email):
    try:
        validatedEmail = validate_email(email)
        email = validatedEmail.ascii_email
    except EmailNotValidError:
        return False
    return True

def validatePasswordStrength(password):
    policy = PasswordPolicy.from_names(
        length=8,
        uppercase=1,
        numbers=1,
        special=1,
    )
    
    return len(policy.test(password)) == 0

def passwordsEqual(psw1, psw2):
    return psw1 == psw2

def encryptPassword(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')