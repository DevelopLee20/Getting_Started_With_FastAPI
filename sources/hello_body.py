from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/hi")
def greet(who: str = Body(embed=True)): # embed: "Mom"이 아니라 {"who": "Mom"} 으로 되어야 한다는 뜻
    return f"Hello? {who}?"
