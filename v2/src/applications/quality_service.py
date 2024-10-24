from ..core.entities.summary import Summary
from ..core.interfaces.services import QualityCheckService
from typing import List

class QualityService:
    def __init__(self, quality_service: QualityCheckService):
        self.quality_service = quality_service
    
    async def check_summaries(self, summaries: List[Summary]) -> List[float]:
        scores = []
        for summary in summaries:
            score = await self.quality_service.check_quality(summary)
            scores.append(score)
        return scores
    
    async def is_summary_acceptable(self, summary: Summary, threshold: float = 0.7) -> bool:
        score = await self.quality_service.check_quality(summary)
        return score >= threshold