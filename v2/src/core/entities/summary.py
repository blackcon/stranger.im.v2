from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict

@dataclass
class Summary:
    id: str
    content_id: str
    summary_text: str
    created_at: datetime
    quality_score: float
    metadata: Optional[Dict] = None