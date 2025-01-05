from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/hi")
def greet(who: str = Header()): # greeting 인자를 HTTP 헤더로 전달
    return f"Hello? {who}?"
