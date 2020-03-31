import uuid
from typing import Optional

import bcrypt
from cryptography.fernet import Fernet, InvalidToken

from {{cookiecutter.project_name}}.config import SECRET_KEY

app_secret_key = Fernet(SECRET_KEY)


def get_common_key():
    return app_secret_key


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"),
                              hashed_password.encode("utf-8"))
    except ValueError:  # ValueError: Invalid salts
        return False


def encrypt_data(data: str) -> str:
    encryptor = get_common_key()
    return encryptor.encrypt(data.encode("utf-8")).decode("utf-8")


def decrypt_data(token: str) -> Optional[str]:
    try:
        decryptor = get_common_key()
        return decryptor.decrypt(token.encode("utf-8")).decode("utf-8")
    except InvalidToken:
        return None


def get_session_id():
    return encrypt_data(uuid.uuid1().hex)
