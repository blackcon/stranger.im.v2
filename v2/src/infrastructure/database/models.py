from sqlalchemy import Column, String, Text, Float, DateTime, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ContentModel(Base):
    __tablename__ = "contents"
    
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    original_text = Column(Text, nullable=False)
    source_url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    status = Column(Enum("draft", "summarized", "reviewed", "approved", "rejected"), nullable=False)
    summary = Column(Text)
    metadata = Column(JSON)
    tags = Column(JSON)

class SummaryModel(Base):
    __tablename__ = "summaries"
    
    id = Column(String, primary_key=True)
    content_id = Column(String, nullable=False)
    summary_text = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    quality_score = Column(Float, nullable=False)
    metadata = Column(JSON)