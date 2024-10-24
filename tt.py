# 프로젝트 구조를 tar.gz로 만들기 위한 스크립트
import os
import tarfile
from datetime import datetime

def create_project_structure():
    """프로젝트 디렉토리 구조 생성"""
    directories = [
        "src/core/entities",
        "src/core/interfaces",
        "src/infrastructure/database",
        "src/infrastructure/rss",
        "src/infrastructure/ai",
        "src/applications",
        "src/interfaces/api",
        "src/interfaces/workers",
        "tests/unit",
        "tests/integration",
        "tests/e2e",
        "configs",
        "scripts",
        "requirements"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def create_requirements_files():
    """requirements 파일 생성"""
    requirements = {
        "base.txt": """
fastapi==0.68.1
uvicorn==0.15.0
sqlalchemy==1.4.23
aiohttp==3.8.1
feedparser==6.0.8
openai==0.27.0
pydantic==1.8.2
python-dotenv==0.19.0
""",
        "development.txt": """
-r base.txt
pytest==6.2.5
pytest-asyncio==0.15.1
black==21.7b0
flake8==3.9.2
mypy==0.910
""",
        "production.txt": """
-r base.txt
gunicorn==20.1.0
prometheus-client==0.11.0
sentry-sdk==1.3.1
"""
    }
    
    for filename, content in requirements.items():
        with open(f"requirements/{filename}", "w") as f:
            f.write(content.strip())

def create_readme():
    """README.md 파일 생성"""
    readme_content = """
# Newsletter AI System

## 개요
AI 기반 뉴스레터 자동화 시스템입니다. RSS 피드로부터 콘텐츠를 수집하고, AI를 활용하여 요약을 생성하며, 품질 관리 시스템을 통해 콘텐츠의 품질을 보장합니다.

## 주요 기능
- RSS 피드 수집
- AI 기반 콘텐츠 요약
- 품질 관리 시스템
- 피드백 시스템

## 설치 방법
1. Python 3.8 이상 설치
2. 의존성 설치:
   ```bash
   pip install -r requirements/development.txt
   ```
3. 환경 변수 설정:
   - `.env.example`을 `.env`로 복사하고 설정 입력

## 실행 방법
```bash
uvicorn src.main:app --reload
```

## API 문서
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 테스트
```bash
pytest tests/
```

## 라이선스
MIT License
"""
    with open("README.md", "w") as f:
        f.write(readme_content.strip())

def create_env_example():
    """환경 변수 예제 파일 생성"""
    env_content = """
DATABASE_URL=postgresql+asyncpg://user:password@localhost/newsletter
RSS_FEED_URLS=["https://example.com/feed1.xml","https://example.com/feed2.xml"]
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4
RSS_COLLECT_INTERVAL=3600
SUMMARY_PROCESS_INTERVAL=300
QUALITY_THRESHOLD=0.7
"""
    with open(".env.example", "w") as f:
        f.write(env_content.strip())

def create_package():
    """프로젝트를 tar.gz로 패키징"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    package_name = f"newsletter_ai_system_{timestamp}.tar.gz"
    
    with tarfile.open(package_name, "w:gz") as tar:
        # Add all directories and files
        for root, dirs, files in os.walk("."):
            for file in files:
                file_path = os.path.join(root, file)
                # Exclude git files and pycache
                if ".git" not in file_path and "__pycache__" not in file_path:
                    tar.add(file_path)
    
    return package_name

def main():
    """메인 실행 함수"""
    # Create project structure
    create_project_structure()
    
    # Create necessary files
    create_requirements_files()
    create_readme()
    create_env_example()
    
    # Copy all the source files we created earlier
    # (이전에 생성한 모든 소스 파일들을 해당 디렉토리에 복사)
    
    # Create package
    package_name = create_package()
    print(f"Project packaged successfully: {package_name}")

if __name__ == "__main__":
    main()
