# Getting_Started_With_FastAPI

```text
rep: 처음 시작하는 FastAPI, 빌 루바노빅, 한빛미디어
```

- [Getting\_Started\_With\_FastAPI](#getting_started_with_fastapi)
  - [독서 기록](#독서-기록)
  - [단어 정리](#단어-정리)
  - [FastAPI](#fastapi)
    - [FastAPI 코드](#fastapi-코드)
    - [FastAPI OpenAPI](#fastapi-openapi)
  - [동시성](#동시성)
  - [비동기식 시스템](#비동기식-시스템)
  - [책에서 사용되는 계층](#책에서-사용되는-계층)
  - [파이썬 관련](#파이썬-관련)
    - [타입 힌트](#타입-힌트)
    - [파이썬 관련 툴](#파이썬-관련-툴)
    - [파이썬 pylance](#파이썬-pylance)
    - [__init__.py](#initpy)
  - [테스트](#테스트)
    - [pytest](#pytest)
  - [웹 Web](#웹-web)
    - [웹 정의](#웹-정의)
    - [CRUD](#crud)
    - [상태 코드](#상태-코드)
    - [응답 유형](#응답-유형)
    - [response 클래스에 필요한 요소](#response-클래스에-필요한-요소)
    - [request, model, response](#request-model-response)
    - [일반적인 Restful url 규칙](#일반적인-restful-url-규칙)
  - [의존성](#의존성)
    - [의존성 관련 문제](#의존성-관련-문제)
    - [의존성 주입 방법](#의존성-주입-방법)
  - [인사이트](#인사이트)

## 독서 기록

|date|page start|page end|
|---|---|---|
| 2025-01-02 | 1 | 36 |
| 2025-01-03 | 37 | 50 |
| 2025-01-05 | 51 | 74 |
| 2025-01-14 | 75 | 106 |
| 2025-01-15 | 107 | 114 |
| 2025-02-06 | 115 | 138 |
|---|---|---|

## 단어 정리

| 단어 | 영문 | 뜻 |
|---|---|---|
| 스코프 | scope | 동일한 객체를 가리키는 코드 영역 |
| 웹 서버 게이트웨이 인터페이스 | WSGI | 동기식 웹 서버 연결 방식 |
| 파이썬 비동기 서버 게이트웨이 인터페이스 | ASGI | 비동기식 웹 서버 연결 방식 |
| 유스케이스 | Use case | 행위자가 일을 달성하기 위한 시나리오 집합 명시 |
| 보일러플레이트 코드 | Boilerplate Code | 최소한의 수정으로 여러 곳에 필수적으로 사용되는 코드 |
| 의존성 | dependency | 어떤 시점에 필요한 특정 정보 |
| 헬퍼 함수 | Helper Functions | 함수 안에서 다른 함수의 값을 반환하는 함수 |
| 스텁 | stub | 동작 중인 모듈을 호출하지 않고 반환되는 미리 준비된 응답 |
|---|---|---|

## FastAPI

### FastAPI 코드

> FastAPI의 웹 코드는 대부분 Starlette 패키지를 기반으로 한다.

- response_model: 반환할 정보를 해당 객체로 변경

### FastAPI OpenAPI

- localhost:8000/docs: 자동 API 문서화 기능
- localhost:8000/redoc: 사용자 친화적인 API 문서화 기능

## 동시성

> 서비스의 성장을 위해서 효율성과 확장성을 올리는 것, 아래 두 가지 항목이 줄어야 한다.

- 지연 시간 latency: 사전 대기 시간
- 처리량 throughput: 서비스와 호출자 간의 초당 바이트 수

## 비동기식 시스템

- 이벤트 루프에 작업 요청을 보낸 후 표시.
- 보낸 작업이 이벤트 루프에서 시작됐다는 즉각적인 응답을 받고 넘어감.
- 보내진 작업의 결과는 작업이 완료된 후 처리됨.
- async와 await를 무작정 사용한다고 해서 더 빠르게 실행되지 않고, 비동기 설정하는 오버헤드 때문에 조금 더 느려질 수 있음.
- I/O를 오래 기다리지 않기 위해서 사용됨

## 책에서 사용되는 계층

- 웹: 클라이언트의 요청을 수집하고, 서비스 계층을 호출해 응답을 반환하는 계층
- 서비스: 필요할 때 데이터 계층을 호출하는 비즈니스 로직
- 데이터: 데이터 저장소 및 기타 서비스에 접근
- 모델: 모든 계층이 공유하는 데이터 정의
- 웹 클라이언트: 웹 브라우저 또는 기타 클라이언트 측 소프트웨어
- 데이터베이스: 데이터 저장소

![수직 계층](/src/수직%20계층.png)

## 파이썬 관련

### 타입 힌트

- 타입 힌트는 3.6 이상에서 제공하는 기능
- 파이썬 버전 3.9 이전에서는 typing 라이브러리의 데이터 타입을 사용해야 한다.
- 파이썬 3.10 이상에서는 Union[type1 | type2]를 type1 | type2 의 형태로 작성한다.

### 파이썬 관련 툴

- Poetry: 가상환경 관리
- black: 코드 포매팅
- pytest: 테스팅 관리
- pre-commit: 지속적 통합 제공
- mypy: 타입 힌트 검사기

### 파이썬 pylance

```python
from pydantic import BaseModel, constr, conint, conlist, Field

class Creature(BaseModel):
    name: constr(min_length=2)        # 형식 식에는 호출 식을 사용할 수 없습니다.
    age: conint(gt=2)                 # 형식 식에는 호출 식을 사용할 수 없습니다.
    job: conlist(str, min_length=2)   # 형식 식에는 호출 식을 사용할 수 없습니다.
    note: Field(..., min_length=2)    
```

> pylance는 해당 코드에 문제를 발생시킨다(문법적으로 문제없음). 아래는 대안이다.

```python
from pydantic import BaseModel, constr, conint, conlist, Field

class Creature(BaseModel):
    name: str = constr(min_length=2)        # 최소 길이 지정
    age: int = conint(gt=2)                 # 최소 값 지정
    job: list = conlist(str, min_length=2)  # 데이터 타입과 최소 길이 지정
    note: str = Field(..., min_length=2)    # ...은 기본값이 필요없음, 다른 타입의 대안으로 사용
```

### __init__.py

- 폴더 내에 존재하면 해당 디렉터리를 import 할 수 있는 패키지로 취급함
- 디렉토리가 하위 계층을 빌드할 때 상위 계층에 일부 스텁 데이터를 제공함

## 테스트

- requests: http 요청을 보내는 라이브러리
- httpx: 비동기 http 요청을 보낼 때 유용한 라이브러리

### pytest

- fixture: 테스트 함수들이 공통적으로 사용할 데이터 설정 및 초기화, 다른 테스트 함수에 자동으로 전달됨(재사용성 증가, 코드 중복 감소)
- with pytest.raises(Exception): 테스트시 해당 코드에서 에러가 발생됨을 확인

## 웹 Web

### 웹 정의

- Header: HTTP 헤더
- Path: URL
- Query: 쿼리 매개변수 (URL 끝의 ? 뒤), localhost:8000/docs?
- Body: HTTP 본문

> 혹시나 RESTful 원칙을 강요하는 검사가 우리를 고소한다면, 대단한 법원이나 구경하고 오라한다.

### CRUD

- POST: 만들기(쓰기)
- PUT: 전체 수정(갈아 끼우기)
- PATCH: 부분 수정(고치기)
- GET: 가져오기(읽기, 찾기)
- DELETE: 삭제

### 상태 코드

- 100번대: 정보, 계속 진행
- 200번대: 성공
- 300번대: 리다이렉션
- 400번대: 클라이언트 오류
- 500번대: 서버 오류

> 상태 코드 중 418은 I'm a teapot(<https://www.google.com/teapot>) 으로 웹에 연결된 찻주전자에 커피를 내리라는 요청을 보내면 반환되는 코드이다. 즉, 이스터에그이다.(서버가 찻주전자이므로 커피 내리기를 거절했다는 코드)

![I'm a tea pot](src/I'm%20a%20teapot.png)

### 응답 유형

- JSONResponse(기본값)
- HTMLResponse
- PlainTextResponse
- RedirectResponse
- FileResponse
- StreamingResponse

### response 클래스에 필요한 요소

- content: 콘텐츠, 문자열 또는 바이트 형식
- media_type: 미디어 유형, 문자열 형태의 MIME 유형 값
  - MIME: Multipurpose Internet Mail Extensions, 전자 우편 인터넷 표준
- status_code: 상태 코드
- headers: 헤더, 문자열 dict 형식

### request, model, response

- request: 사용자가 제공해야 하는 정보(TagIn)
- model: 내부에서 사용하지만 외부에 노출되지 않아야 하는 정보(Tag)
- response: 사용자에게 반환할 수 있는 정보(TagOut)

### 일반적인 Restful url 규칙

```sql
<동작> /resource/
```

- resource 유형의 모든 리소스에 <동작>을 적용한다.

```sql
<동작> /resource/id
```

- id가 있는 resource에 <동작>을 적용한다.

## 의존성

> 어떤 시점에 필요한 특정 정보, 정보가 필요한 시점에 바로 가져오는 코드

- 결합도를 낮춤
- 테스트시 모킹(mocking)하기 용이해짐
- 유지보수성 향상

### 의존성 관련 문제

- 테스트: 의존성 테스트를 위해 함수를 변형할 수 없다.
- 숨겨진 의존성: 의존성의 세부 사항을 숨기면 외부 코드가 변경될 때, 우리가 작성한 코드가 망가질 수 있다.
- 중복 호출: 의존성이 공통으로 사용되면 여러 함수에서 중복으로 호출될 수 있다.

### 의존성 주입 방법

- 헬퍼 함수를 전달한 다음, 이를 호출해 특정 데이터를 가져옴

## 인사이트

- GraphQL(<https://graphql.org>)
- NewSQL
- 그린스레드
