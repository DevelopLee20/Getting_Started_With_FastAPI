from fastapi import FastAPI

app = FastAPI()

@app.get("/happy")
def happy(status_code=404): # NOTE: 상태 코드 변경되지 않음
    return ":)"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("http_status_code_select:app", reload=True)
