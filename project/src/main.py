from fastapi import FastAPI
from web import explorer

app = FastAPI()
app.include_router(explorer.router)

@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True) # main.py 파일 변경시 재시작
