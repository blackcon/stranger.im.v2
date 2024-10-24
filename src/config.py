from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    RSS_FEED_URLS: List[str]
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4"
    RSS_COLLECT_INTERVAL: int = 3600
    SUMMARY_PROCESS_INTERVAL: int = 300
    QUALITY_THRESHOLD: float = 0.7
    
    class Config:
        env_file = ".env"