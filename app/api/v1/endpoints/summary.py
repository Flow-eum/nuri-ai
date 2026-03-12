from fastapi import APIRouter, Depends

from app.api.deps import verify_token
from app.schemas.summary import SummaryRequest, SummaryResponse
from app.services.summary_service import SummaryService

router = APIRouter()

@router.post("/", response_model=SummaryResponse, dependencies=[Depends(verify_token)])
async def summarize(
        request: SummaryRequest,
        service: SummaryService = Depends()
):
    return await service.generate_summary(request)