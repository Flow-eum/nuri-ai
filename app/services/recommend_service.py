import json
from openai import OpenAI
from app.core.config import settings
from app.schemas.recommend import RecommendRequest, RecommendResponse

class RecommendService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.SUMMARY_MODEL

    async def get_plan_recommendation(self, data: RecommendRequest) -> RecommendResponse:
        prompt = f"""
        주제: {data.topic}
        기간: {data.days}
        강조 사항: {data.focus}
        위 조건에 맞는 계획을 세워줘. 응답은 반드시 JSON 형식을 지켜줘.
        형식 예시: {{"title": "...", "daily_plan": [{{"time": "...", "activity": "..."}}], "advice": "..."}}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return RecommendResponse(**result)