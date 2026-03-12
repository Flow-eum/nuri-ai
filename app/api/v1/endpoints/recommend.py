from fastapi import APIRouter, Depends

from app.api.deps import verify_token
from app.schemas.recommend import RecommendRequest, RecommendResponse
from app.services.recommend_service import RecommendService

router = APIRouter()

@router.post("/", response_model=RecommendResponse, dependencies=[Depends(verify_token)])
async def get_recommendation(
        request: RecommendRequest,
        service: RecommendService = Depends()
):
    return await service.get_plan_recommendation(request)