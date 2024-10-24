from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict
from enum import Enum

class ContentStatus(Enum):
    DRAFT = "draft"
    SUMMARIZED = "summarized"
    REVIEWED = "reviewed"
    APPROVED = "approved"
    REJECTED = "rejected"

@dataclass
class Content:
    id: str
    title: str
    original_text: str
    source_url: str
    created_at: datetime
    status: ContentStatus
    summary: Optional[str] = None
    metadata: Optional[Dict] = None
    tags: List[str] = None
    
    def update_summary(self, summary: str):
        self.summary = summary
        self.status = ContentStatus.SUMMARIZED
    
    def approve(self):
        self.status = ContentStatus.APPROVED
    
    def reject(self):
        self.status = ContentStatus.REJECTED