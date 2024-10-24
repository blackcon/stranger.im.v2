import asyncio
from datetime import datetime
from typing import List
import logging
from ...infrastructure.rss.collector import RSSCollector
from ...applications.content_service import ContentService

logger = logging.getLogger(__name__)

class RSSWorker:
    def __init__(
        self,
        feed_urls: List[str],
        content_service: ContentService,
        collect_interval: int = 3600  # 1시간
    ):
        self.collector = RSSCollector(feed_urls)
        self.content_service = content_service
        self.collect_interval = collect_interval
    
    async def start(self):
        while True:
            try:
                logger.info("Starting RSS collection...")
                contents = await self.collector.collect()
                
                for content in contents:
                    try:
                        await self.content_service.create_content(content)
                        logger.info(f"Saved content: {content.title}")
                    except Exception as e:
                        logger.error(f"Error saving content: {str(e)}")
                
                logger.info(f"Completed RSS collection. Found {len(contents)} articles")
                await asyncio.sleep(self.collect_interval)
            
            except Exception as e:
                logger.error(f"Error in RSS collection: {str(e)}")
                await asyncio.sleep(60)  # 오류 발생시 1분 후 재시도