from abc import ABC, abstractmethod
from ..entities.content import Content
from ..entities.summary import Summary

class SummaryService(ABC):
    @abstractmethod
    async def generate_summary(self, content: Content) -> Summary:
        pass

class QualityCheckService(ABC):
    @abstractmethod
    async def check_quality(self, summary: Summary) -> float:
        pass