from fastapi import APIRouter, Depends
from app.schemas.summary import SummaryRequest, SummaryResponse
from app.services.summary_service import SummaryService

router = APIRouter()

async def summarize(
        request: SummaryRequest,
        service: SummaryService = Depends()
):
    return await service.generate_summary(request)