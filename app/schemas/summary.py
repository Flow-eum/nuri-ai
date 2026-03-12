from pydantic import BaseModel, Field
from typing import Optional

class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=20, description="요약할 원본 텍스트")
    max_words: Optional[int] = Field(default=100, description="요약본의 희망 단어 수")

class SummaryResponse(BaseModel):
    summary: str = Field(..., description="생성된 요약 내용")
    model_used: str = Field(..., description="사용된 LLM 모델명")
    processing_time: float = Field(..., description="소요 시간(초)")