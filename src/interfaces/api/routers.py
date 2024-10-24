from fastapi import APIRouter, HTTPException, Depends
from typing import List
from .schemas import (
    ContentCreate,
    ContentResponse,
    SummaryResponse,
    FeedbackCreate
)
from ...applications.content_service import ContentService
from ...applications.summary_service import SummaryApplicationService
from ...applications.feedback_service import FeedbackService
from ...core.entities.content import Content
from ...core.entities.feedback import Feedback
from datetime import datetime
import uuid

router = APIRouter()

def get_content_service() -> ContentService:
    # 의존성 주입 설정
    # 실제 구현에서는 데이터베이스 세션 등을 주입
    pass

def get_summary_service() -> SummaryApplicationService:
    pass

def get_feedback_service() -> FeedbackService:
    pass

@router.post("/contents", response_model=ContentResponse)
async def create_content(
    content_data: ContentCreate,
    content_service: ContentService = Depends(get_content_service)
):
    content = Content(
        id=str(uuid.uuid4()),
        title=content_data.title,
        original_text=content_data.original_text,
        source_url=content_data.source_url,
        created_at=datetime.now(),
        status=ContentStatus.DRAFT,
        tags=content_data.tags,
        metadata=content_data.metadata
    )
    
    created_content = await content_service.create_content(content)
    return ContentResponse.from_orm(created_content)

@router.get("/contents/{content_id}", response_model=ContentResponse)
async def get_content(
    content_id: str,
    content_service: ContentService = Depends(get_content_service)
):
    content = await content_service.get_content(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return ContentResponse.from_orm(content)

@router.post("/contents/{content_id}/process")
async def process_content(
    content_id: str,
    content_service: ContentService = Depends(get_content_service)
):
    try:
        content = await content_service.process_content(content_id)
        return ContentResponse.from_orm(content)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/contents/{content_id}/summary", response_model=SummaryResponse)
async def get_summary(
    content_id: str,
    summary_service: SummaryApplicationService = Depends(get_summary_service)
):
    summary = await summary_service.get_summary(content_id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return SummaryResponse.from_orm(summary)

@router.post("/feedback", status_code=201)
async def create_feedback(
    feedback_data: FeedbackCreate,
    feedback_service: FeedbackService = Depends(get_feedback_service)
):
    feedback = Feedback(
        id=str(uuid.uuid4()),
        content_id=feedback_data.content_id,
        feedback_type=feedback_data.feedback_type,
        score=feedback_data.score,
        comment=feedback_data.comment,
        created_at=datetime.now()
    )
    
    created_feedback = await feedback_service.save_feedback(feedback)
    return {"message": "Feedback saved successfully", "id": created_feedback.id}