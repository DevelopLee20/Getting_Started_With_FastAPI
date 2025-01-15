from fastapi import FastAPI, Depends, Query

app = FastAPI()

# 의존성 함수
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "gender": gender}

# 경로 함수
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:   # 의존성 주입으로 name과 gender를 요청함
    return user

# 경로 함수
@app.get("/user", dependencies=[Depends(user_dep)])     # 의존성을 정의해도 됨
def get_user() -> dict:
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("dependency:app", reload=True)
