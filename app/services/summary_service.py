import time
from openai import OpenAI
from app.core.config import settings
from app.schemas.summary import SummaryRequest, SummaryResponse

class SummaryService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.SUMMARY_MODEL
    async def generate_summary(self, data: SummaryRequest) -> SummaryResponse:
        start_time = time.time()

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": f"당신은 전문 요약가입니다. 내용을 {data.max_words} 단어 내외로 요약하세요."},
                {"role": "user", "content": data.text}
            ],
            temperature=settings.SUMMARY_TEMPERATURE
        )

        summary_text = response.choices[0].message.content
        duration = round(time.time() - start_time, 2)

        return SummaryResponse(
            summary = summary_text,
            model_used=self.model,
            processing_time=duration
        )