import httpx
from fastapi import Depends,HTTPException, status, Request
from clerk_backend_api.security import AuthenticateRequestOptions
from app.core.config import settings
from app.core.clerk import clerk

class AuthUser:
    def __init__(self):
        pass 