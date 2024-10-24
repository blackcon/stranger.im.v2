from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Enum

class FeedbackType(Enum):
    SUMMARY_QUALITY = "summary_quality"
    CONTENT_RELEVANCE = "content_relevance"
    GENERAL = "general"

@dataclass
class Feedback:
    id: str
    content_id: str
    feedback_type: FeedbackType
    score: float
    comment: Optional[str]
    created_at: datetime