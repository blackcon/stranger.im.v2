import feedparser
import aiohttp
from datetime import datetime
from typing import List, Dict
from ...core.entities.content import Content, ContentStatus

class RSSCollector:
    def __init__(self, feed_urls: List[str]):
        self.feed_urls = feed_urls
    
    async def collect(self) -> List[Content]:
        contents = []
        async with aiohttp.ClientSession() as session:
            for url in self.feed_urls:
                feed = await self._fetch_feed(session, url)
                contents.extend(self._parse_feed(feed))
        return contents
    
    async def _fetch_feed(self, session: aiohttp.ClientSession, url: str) -> Dict:
        async with session.get(url) as response:
            text = await response.text()
            return feedparser.parse(text)
    
    def _parse_feed(self, feed: Dict) -> List[Content]:
        contents = []
        for entry in feed.entries:
            content = Content(
                id=str(hash(entry.link)),
                title=entry.title,
                original_text=entry.description,
                source_url=entry.link,
                created_at=datetime.now(),
                status=ContentStatus.DRAFT,
                tags=[tag.term for tag in entry.get('tags', [])]
            )
            contents.append(content)
        return contents