import asyncio
from fastapi import FastAPI
from .interfaces.api.routes import router
from .interfaces.workers.rss_worker import RSSWorker
from .interfaces.workers.summary_worker import SummaryWorker
from .config import Settings
from .dependencies import get_content_service

app = FastAPI(title="Newsletter AI System")
settings = Settings()

@app.on_event("startup")
async def startup_event():
    # Start background workers
    content_service = await get_content_service()
    
    rss_worker = RSSWorker(
        feed_urls=settings.RSS_FEED_URLS,
        content_service=content_service,
        collect_interval=settings.RSS_COLLECT_INTERVAL
    )
    
    summary_worker = SummaryWorker(
        content_service=content_service,
        process_interval=settings.SUMMARY_PROCESS_INTERVAL
    )
    
    asyncio.create_task(rss_worker.start())
    asyncio.create_task(summary_worker.start())

app.include_router(router, prefix="/api/v1")