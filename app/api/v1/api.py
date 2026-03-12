from fastapi import APIRouter
from app.api.v1.endpoints import summary

api_router = APIRouter()

api_router.include_router(summary.router, prefix="/summary", tags=["Summary"])