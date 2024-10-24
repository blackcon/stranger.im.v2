from typing import Optional
import openai
from ...core.interfaces.services import SummaryService
from ...core.entities.content import Content
from ...core.entities.summary import Summary
from datetime import datetime

class OpenAISummarizer(SummaryService):
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key
    
    async def generate_summary(self, content: Content) -> Summary:
        prompt = f"""Please summarize the following article:
Title: {content.title}
Content: {content.original_text}
Please provide a concise summary that captures the main points."""
        
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        summary_text = response.choices[0].message.content
        
        return Summary(
            id=str(hash(f"{content.id}_summary")),
            content_id=content.id,
            summary_text=summary_text,
            created_at=datetime.now(),
            quality_score=0.0  # Will be updated by quality checker
        )