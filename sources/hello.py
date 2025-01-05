from fastapi import FastAPI

app = FastAPI() # 최상위 FastAPI 객체

@app.get("/hi") # 경로 데코레이터
def greet():    # 경로 함수
    return "Hello? World?"

if __name__ == "__main__":  # 내부적으로 uvicorn 시작
    import uvicorn

    uvicorn.run("hello:app", reload=True)
