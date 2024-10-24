from typing import List, Optional
from ..core.entities.content import Content, ContentStatus
from ..core.interfaces.repositories import ContentRepository
from ..core.interfaces.services import SummaryService, QualityCheckService

class ContentService:
    def __init__(
        self,
        content_repository: ContentRepository,
        summary_service: SummaryService,
        quality_service: QualityCheckService
    ):
        self.content_repository = content_repository
        self.summary_service = summary_service
        self.quality_service = quality_service
    
    async def create_content(self, content: Content) -> Content:
        return await self.content_repository.save(content)
    
    async def get_content(self, content_id: str) -> Optional[Content]:
        return await self.content_repository.get_by_id(content_id)
    
    async def process_content(self, content_id: str) -> Content:
        content = await self.get_content(content_id)
        if not content:
            raise ValueError(f"Content not found: {content_id}")
        
        # Generate summary
        summary = await self.summary_service.generate_summary(content)
        
        # Check quality
        quality_score = await self.quality_service.check_quality(summary)
        summary.quality_score = quality_score
        
        # Update content with summary
        content.update_summary(summary.summary_text)
        return await self.content_repository.save(content)