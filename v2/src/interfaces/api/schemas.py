from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict
from ...core.entities.content import ContentStatus
from ...core.entities.feedback import FeedbackType

class ContentCreate(BaseModel):
    title: str
    original_text: str
    source_url: str
    tags: Optional[List[str]] = None
    metadata: Optional[Dict] = None

class ContentResponse(BaseModel):
    id: str
    title: str
    original_text: str
    source_url: str
    created_at: datetime
    status: ContentStatus
    summary: Optional[str]
    tags: Optional[List[str]]
    metadata: Optional[Dict]

class SummaryResponse(BaseModel):
    id: str
    content_id: str
    summary_text: str
    created_at: datetime
    quality_score: float
    metadata: Optional[Dict]

class FeedbackCreate(BaseModel):
    content_id: str
    feedback_type: FeedbackType
    score: float
    comment: Optional[str]