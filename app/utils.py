from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pwd(password):
    return pwd_context.hash(password)

def verify_pwd(user_pwd, hashed_pwd):
    return pwd_context.verify(user_pwd, hashed_pwd)