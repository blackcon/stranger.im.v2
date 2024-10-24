import asyncio
import logging
from ...applications.content_service import ContentService
from ...core.entities.content import ContentStatus

logger = logging.getLogger(__name__)

class SummaryWorker:
    def __init__(
        self,
        content_service: ContentService,
        batch_size: int = 10,
        process_interval: int = 300  # 5분
    ):
        self.content_service = content_service
        self.batch_size = batch_size
        self.process_interval = process_interval
    
    async def start(self):
        while True:
            try:
                logger.info("Starting summary processing...")
                pending_contents = await self.content_service.get_pending_contents(
                    status=ContentStatus.DRAFT,
                    limit=self.batch_size
                )
                
                for content in pending_contents:
                    try:
                        await self.content_service.process_content(content.id)
                        logger.info(f"Processed content: {content.title}")
                    except Exception as e:
                        logger.error(f"Error processing content: {str(e)}")
                
                await asyncio.sleep(self.process_interval)
            
            except Exception as e:
                logger.error(f"Error in summary processing: {str(e)}")
                await asyncio.sleep(60)