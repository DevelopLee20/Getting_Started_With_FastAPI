from fastapi import FastAPI

app = FastAPI()

@app.get("hi/{who}")    # who URL 경로 변수 설정
def greet(who):
    return f"Hello? {who}?"
