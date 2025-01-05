from fastapi import Response, FastAPI

app = FastAPI()

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):  # response: response 객체(반환하지 않아도 됨)
    response.headers[name] = value

    return "normal body"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello_header_select:app", reload=True)
