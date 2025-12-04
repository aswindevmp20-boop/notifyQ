from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash password using bcrypt safely."""
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """Verify a plain password against its hash."""
    return pwd_context.verify(password, hashed)
