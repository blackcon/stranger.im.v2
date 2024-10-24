from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .config import Settings
from .infrastructure.database.repositories import SQLContentRepository
from .infrastructure.ai.summarizer import OpenAISummarizer
from .infrastructure.ai.quality_checker import OpenAIQualityChecker
from .applications.content_service import ContentService
from .applications.summary_service import SummaryApplicationService
from .applications.quality_service import QualityService
from .applications.feedback_service import FeedbackService

settings = Settings()

# Database
engine = create_async_engine(settings.DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)

async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session

# Repositories
async def get_content_repository():
    session = await get_db_session()
    return SQLContentRepository(session)

# Services
def get_summary_service():
    return OpenAISummarizer(
        api_key=settings.OPENAI_API_KEY,
        model=settings.OPENAI_MODEL
    )

def get_quality_service():
    return OpenAIQualityChecker(
        api_key=settings.OPENAI_API_KEY,
        model=settings.OPENAI_MODEL
    )

# Application Services
async def get_content_service():
    content_repository = await get_content_repository()
    summary_service = get_summary_service()
    quality_service = get_quality_service()
    return ContentService(
        content_repository=content_repository,
        summary_service=summary_service,
        quality_service=quality_service
    )