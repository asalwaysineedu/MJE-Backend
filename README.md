<div align="center">

# 🗓️ MJE Backend

**20~30대를 위한 맞춤형 데이트코스 추천 서비스**

지역 · 시간 · 이동수단 · 동행 정보를 입력하면<br/>
취향에 맞는 데이트 코스를 자동으로 추천해주는 백엔드 API 서버입니다.

</div>

---

## 📖 목차

- [프로젝트 소개](#-프로젝트-소개)
- [시작 가이드](#-시작-가이드)
- [기술 스택](#-기술-스택)
- [주요 기능](#-주요-기능)
- [API 문서](#-api-문서)
- [아키텍처](#-아키텍처)
- [프로젝트 구조](#-프로젝트-구조)

---

## 🌟 프로젝트 소개

**MJE Backend** 는 사용자의 조건(지역, 시작 시간, 이동수단 등)을 입력받아
코스 후보를 생성·점수화·선별하여 최적의 데이트 코스를 추천하는 서비스입니다.

- 코스 추천 및 상세 조회 (장소·카페·맛집·액티비티)
- 사용자 행동 이벤트 트래킹 (홈 / 코스 / 내보내기)
- FastAPI 기반 **Layered Architecture + DDD** 구조

---

## 🚀 시작 가이드

### Requirements

이 프로젝트를 실행하기 위해 아래 환경이 필요합니다.

- **Python** 3.10+
- **MySQL** 8.0
- **Redis** 7.x

### Installation

```bash
# 1. 저장소 클론
git clone https://github.com/EDDI-RobotAcademy/MJE-Backend.git
cd MJE-Backend

# 2. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. 의존성 설치
pip install -r requirements.txt
```

### Environment

루트 디렉토리에 `.env` 파일을 생성하고 아래 값을 채워주세요.

```env
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3307
MYSQL_SCHEMA=mje
REDIS_URL=redis://localhost:6379
CORS_ORIGINS=["http://localhost:3000"]
KAKAO_MAP_REST_API_KEY=your_kakao_key
```

### Run

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 33333
```

서버 실행 후 [http://localhost:33333/docs](http://localhost:33333/docs) 에서 Swagger 문서를 확인할 수 있습니다.

### Run with Docker

MySQL · Redis · Backend 를 한 번에 띄우려면 Docker Compose 를 사용하세요.

```bash
docker-compose up -d
```

---

## 🛠 기술 스택

### Environment

![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=flat&logo=gunicorn&logoColor=white)

### Database & Cache

![MySQL](https://img.shields.io/badge/MySQL_8.0-4479A1?style=flat&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)

### Config & Tools

![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-6BA81E?style=flat&logo=alembic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

| 분류 | 사용 기술 |
| --- | --- |
| Language | Python 3.10+ |
| Framework | FastAPI, Uvicorn |
| Database | MySQL 8.0 (SQLAlchemy async, aiomysql) |
| Cache | Redis (redis[asyncio]) |
| Config | Pydantic Settings, python-dotenv |
| Migration | Alembic |
| HTTP Client | httpx |
| Infra | Docker, Docker Compose |

---

## ✨ 주요 기능

### 🧭 코스 추천
- 사용자 조건(지역·시간·이동수단·동행) 기반 코스 후보 생성
- 점수화(Scoring) 및 선별(Selection)을 통한 최적 코스 추천
- 코스 소요 시간 자동 계산

### 📍 코스 상세 조회
- 코스 상세 정보 및 포함 장소 조회
- 카테고리별 조회: 맛집 · 카페 · 액티비티
- 다른 추천 코스 함께 보기

### 📊 이벤트 트래킹
사용자 행동 로그를 도메인별로 수집합니다.

| 도메인 | 이벤트 |
| --- | --- |
| **home** | `view_home`, `logo_click`, `home_click` |
| **courses** | `course_create`, `card_click`, `tryagain_click`, `optioncard_click`, `return_click` |
| **export_logs** | `course_export`, `course_send`, `export_close` |

---

## 📡 API 문서

서버 실행 후 자동 생성되는 문서를 통해 전체 API 명세를 확인할 수 있습니다.

- **Swagger UI**: `http://localhost:33333/docs`
- **ReDoc**: `http://localhost:33333/redoc`

### 주요 엔드포인트

| Method | Endpoint | 설명 |
| --- | --- | --- |
| `GET` | `/health` | 서버 헬스체크 |
| `POST` | `/home/events` | 홈 이벤트 기록 |
| `POST` | `/courses/recommendations` | 코스 추천 생성 |
| `GET` | `/courses/recommendations/{course_id}` | 추천 코스 상세 조회 |
| `GET` | `/courses/{course_id}` | 코스 상세 조회 |
| `POST` | `/courses/events` | 코스 이벤트 기록 |
| `GET` | `/recommendations/courses/{course_id}` | 코스 상세 (프론트엔드용) |
| `GET` | `/recommendations/detail/{course_id}/other-courses` | 다른 코스 목록 |
| `GET` | `/recommendations/detail/{course_id}/activities` | 액티비티 목록 |
| `GET` | `/recommendations/detail/{course_id}/cafes` | 카페 목록 |
| `GET` | `/recommendations/detail/{course_id}/restaurants` | 맛집 목록 |
| `POST` | `/api/v1/export-logs` | 코스 내보내기 로그 기록 |

---

## 🏗 아키텍처

본 프로젝트는 **Layered Architecture + Domain Driven Design (DDD)** 를 따릅니다.

### 의존성 방향

```
Controller → Service → Domain
                ↓
        Repository Interface → Repository Implementation → Infrastructure
```

- 의존성은 항상 하위 계층으로만 흐릅니다.
- **Domain** 은 어떠한 외부 기술(FastAPI / SQLAlchemy / Redis 등)도 알지 못하는 순수 Python 으로 작성합니다.
- **Infrastructure** 는 모든 기술 의존성을 포함합니다.

### 데이터 흐름

```
Client → Controller → Service → Domain → Repository → Infrastructure
```

### 계층별 책임

| 계층 | 책임 |
| --- | --- |
| **Controller** | HTTP 요청 수신, Form ↔ DTO 변환, Service 호출 |
| **Service** | 유스케이스 실행 흐름, 트랜잭션 경계, Domain Event 발행 |
| **Domain** | 비즈니스 규칙·상태·불변성 보장 (순수 Python) |
| **Repository** | 데이터 접근 추상화, Domain 기준 영속성 제공 |
| **Infrastructure** | DB / Cache / External API / Config 구현 |

---

## 📂 프로젝트 구조

```
app
 ├ domains
 │   ├ home               # 홈 화면 이벤트
 │   ├ recommendation     # 코스 추천 · 상세 조회
 │   └ courses            # 코스 생성 · 이벤트
 │       ├ domain         # entity · value_object · events · service
 │       ├ service        # usecase · dto(request/response)
 │       ├ controller     # api(request_form/response_form)
 │       └ repository     # orm · mapper
 │
 ├ common                 # 공통 예외 처리
 │
 ├ infrastructure
 │   ├ database           # DB 연결 · ORM
 │   ├ cache              # Redis Client
 │   ├ api/export_logs    # 인프라 레벨 내보내기 로그
 │   └ config             # 환경 변수 설정
 │
 └ main.py                # FastAPI 진입점
```
