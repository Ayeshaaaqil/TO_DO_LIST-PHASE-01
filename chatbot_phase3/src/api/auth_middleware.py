"""
Authentication Middleware for the API

This module provides authentication functionality for the API,
ensuring that only authenticated users can access protected endpoints.
"""
from typing import Optional
import uuid
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

security = HTTPBearer()

# JWT configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"


def verify_token(token: str) -> Optional[uuid.UUID]:
    """
    Extract user ID from JWT token.
    Decode the JWT and return the user ID.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
        return uuid.UUID(user_id)
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )


def get_current_user(credentials: HTTPAuthorizationCredentials = security):
    """
    Get the current user from the token in the request.
    """
    token = credentials.credentials
    return verify_token(token)