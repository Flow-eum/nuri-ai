from pydantic import BaseModel, Field
from typing import List

class TaskItem(BaseModel):
    time: str = Field(..., description="수행 시간 (예: 오전 10시)")
    activity: str = Field(..., description="할 일 내용")

class RecommendRequest(BaseModel):
    topic: str = Field(..., description="계획 주제")
    days: int = Field(default=1, ge=1, le=7, description="계획 기간 (1~7일)")
    focus: str = Field(default="효율성", description="강조하고 싶은 가치 (예: 휴식, 빽빽한 일정)")

class RecommendResponse(BaseModel):
    title: str
    daily_plan: List[TaskItem]
    advice: str = Field(..., description="LLM의 추가 조언")