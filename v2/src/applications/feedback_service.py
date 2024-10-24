from ..core.entities.feedback import Feedback
from ..core.interfaces.repositories import FeedbackRepository
from typing import List

class FeedbackService:
    def __init__(self, feedback_repository: FeedbackRepository):
        self.feedback_repository = feedback_repository
    
    async def save_feedback(self, feedback: Feedback) -> Feedback:
        return await self.feedback_repository.save(feedback)
    
    async def get_content_feedback(self, content_id: str) -> List[Feedback]:
        return await self.feedback_repository.get_by_content_id(content_id)
    
    async def calculate_average_score(self, content_id: str) -> float:
        feedbacks = await self.get_content_feedback(content_id)
        if not feedbacks:
            return 0.0
        return sum(f.score for f in feedbacks) / len(feedbacks)