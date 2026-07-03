from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "fin_guard_secret_key"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {}

def hash_password(password: str):
    return pwd_context.hash(str(password)[:72])

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return None

def seed_users():
    users_db["admin"] = {
        "password": hash_password("1234"),
        "role": "admin"
    }