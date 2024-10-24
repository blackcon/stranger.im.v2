from ..core.entities.content import Content
from ..core.entities.summary import Summary
from ..core.interfaces.repositories import SummaryRepository
from ..core.interfaces.services import SummaryService, QualityCheckService

class SummaryApplicationService:
    def __init__(
        self,
        summary_repository: SummaryRepository,
        summary_service: SummaryService,
        quality_service: QualityCheckService
    ):
        self.summary_repository = summary_repository
        self.summary_service = summary_service
        self.quality_service = quality_service
    
    async def generate_summary(self, content: Content) -> Summary:
        # Generate summary
        summary = await self.summary_service.generate_summary(content)
        
        # Check quality
        quality_score = await self.quality_service.check_quality(summary)
        summary.quality_score = quality_score
        
        # Save summary
        return await self.summary_repository.save(summary)
    
    async def get_summary(self, content_id: str) -> Summary:
        return await self.summary_repository.get_by_content_id(content_id)