import bcrypt
from cryptography.fernet import Fernet, InvalidToken

from {{cookiecutter.project_name}}.config import SECRET_KEY

app_secret_key = Fernet(SECRET_KEY)


def get_common_key():
    return app_secret_key


def hash_password(password):
    """ hash password
    Args:
        password: a String
    Returns:
        hashed password: a String
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password, hashed_password):
    """ verify password
    Args:
        password: a String
        hashed_password: a String
    Returns:
        a Boolean
    """
    try:
        return bcrypt.checkpw(password.encode("utf-8"),
                              hashed_password.encode("utf-8"))
    except ValueError:  # ValueError: Invalid salts
        return False


def encrypt_token(data):
    encryptor = get_common_key()
    return encryptor.encrypt(data.encode("utf-8"))


def decrypt_token(token):
    try:
        decryptor = get_common_key()
        return decryptor.decrypt(token.encode("utf-8"))
    except InvalidToken:
        return None
