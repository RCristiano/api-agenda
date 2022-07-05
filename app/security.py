import os

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"


def validate_jwt(
    token: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> dict:
    try:
        return jwt.decode(token.credentials, SECRET_KEY,
                          algorithms=[ALGORITHM])
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e
