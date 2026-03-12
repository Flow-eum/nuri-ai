from fastapi import Header, HTTPException, status
from app.core.config import settings

async def verify_token(x_auth_token: str = Header(...)):
    if x_auth_token != settings.API_AUTH_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Auth Token"
        )