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

## 프로젝트 구조
```
newsletter_ai_system/
│
├── src/
│   ├── core/                      # 핵심 도메인 로직
│   │   ├── __init__.py
│   │   ├── entities/              # 도메인 엔티티
│   │   │   ├── content.py
│   │   │   ├── summary.py
│   │   │   └── feedback.py
│   │   └── interfaces/            # 추상 인터페이스
│   │       ├── repositories.py
│   │       └── services.py
│   │
│   ├── infrastructure/            # 외부 시스템 연동
│   │   ├── __init__.py
│   │   ├── database/             # 데이터베이스 관련
│   │   │   ├── models.py
│   │   │   └── repositories.py
│   │   ├── rss/                  # RSS 수집기
│   │   │   ├── collector.py
│   │   │   └── parser.py
│   │   └── ai/                   # AI 엔진 연동
│   │       ├── summarizer.py
│   │       └── quality_checker.py
│   │
│   ├── applications/             # 애플리케이션 서비스
│   │   ├── __init__.py
│   │   ├── content_service.py    # 콘텐츠 관리
│   │   ├── summary_service.py    # 요약 서비스
│   │   ├── quality_service.py    # 품질 관리
│   │   └── feedback_service.py   # 피드백 처리
│   │
│   └── interfaces/               # 인터페이스 레이어
│       ├── __init__.py
│       ├── api/                  # REST API
│       │   ├── routes.py
│       │   └── schemas.py
│       └── workers/              # 백그라운드 작업
│           ├── rss_worker.py
│           └── summary_worker.py
│
├── tests/                        # 테스트 코드
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── configs/                      # 설정 파일
│   ├── development.yaml
│   └── production.yaml
│
├── scripts/                      # 유틸리티 스크립트
│   ├── setup.py
│   └── migrations.py
│
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
│
├── README.md
├── pyproject.toml
└── .env.example
```

## 라이선스
MIT License