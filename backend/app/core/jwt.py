from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi import HTTPException, status
from app.core.config import settings


def create_access_token(data: dict) -> str:
    
    # Create a JWT access token.
    
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return encoded_jwt

def decode_access_token(token: str) -> dict:

    print("=" * 60)
    print("TOKEN:", token)
    print("SECRET:", settings.SECRET_KEY)
    print("ALGORITHM:", settings.ALGORITHM)

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        print("PAYLOAD:", payload)

        return payload

    except JWTError as e:

        print("JWT ERROR:", str(e))

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )