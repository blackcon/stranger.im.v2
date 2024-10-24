from ...core.interfaces.services import QualityCheckService
from ...core.entities.summary import Summary
import openai

class OpenAIQualityChecker(QualityCheckService):
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key
    
    async def check_quality(self, summary: Summary) -> float:
        prompt = f"""Please evaluate the quality of this summary on a scale of 0.0 to 1.0:
Summary: {summary.summary_text}
Consider:
1. Clarity and coherence
2. Completeness of key information
3. Conciseness
4. Grammar and formatting
Provide only the numerical score."""
        
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        try:
            quality_score = float(response.choices[0].message.content.strip())
            return min(max(quality_score, 0.0), 1.0)  # Ensure score is between 0 and 1
        except ValueError:
            return 0.5  # Default score if parsing fails