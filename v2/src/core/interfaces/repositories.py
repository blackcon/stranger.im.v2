from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.content import Content
from ..entities.summary import Summary
from ..entities.feedback import Feedback

class ContentRepository(ABC):
    @abstractmethod
    async def save(self, content: Content) -> Content:
        pass
    
    @abstractmethod
    async def get_by_id(self, content_id: str) -> Optional[Content]:
        pass
    
    @abstractmethod
    async def get_pending_summaries(self) -> List[Content]:
        pass

class SummaryRepository(ABC):
    @abstractmethod
    async def save(self, summary: Summary) -> Summary:
        pass
    
    @abstractmethod
    async def get_by_content_id(self, content_id: str) -> Optional[Summary]:
        pass

class FeedbackRepository(ABC):
    @abstractmethod
    async def save(self, feedback: Feedback) -> Feedback:
        pass
    
    @abstractmethod
    async def get_by_content_id(self, content_id: str) -> List[Feedback]:
        pass