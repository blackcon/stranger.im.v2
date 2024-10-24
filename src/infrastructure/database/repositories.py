from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from ...core.interfaces.repositories import ContentRepository, SummaryRepository
from ...core.entities.content import Content, ContentStatus
from ...core.entities.summary import Summary
from .models import ContentModel, SummaryModel

class SQLContentRepository(ContentRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def save(self, content: Content) -> Content:
        model = ContentModel(
            id=content.id,
            title=content.title,
            original_text=content.original_text,
            source_url=content.source_url,
            created_at=content.created_at,
            status=content.status.value,
            summary=content.summary,
            metadata=content.metadata,
            tags=content.tags
        )
        self.session.add(model)
        await self.session.commit()
        return content
    
    async def get_by_id(self, content_id: str) -> Optional[Content]:
        result = await self.session.get(ContentModel, content_id)
        if not result:
            return None
        return Content(
            id=result.id,
            title=result.title,
            original_text=result.original_text,
            source_url=result.source_url,
            created_at=result.created_at,
            status=ContentStatus(result.status),
            summary=result.summary,
            metadata=result.metadata,
            tags=result.tags
        )