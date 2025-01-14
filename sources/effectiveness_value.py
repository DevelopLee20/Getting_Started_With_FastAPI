from pydantic import BaseModel, constr, conint, conlist, Field

class Creature(BaseModel):
    name: str = constr(min_length=2)        # 최소 길이 지정
    age: int = conint(gt=2)                 # 최소 값 지정
    job: list = conlist(str, min_length=2)  # 데이터 타입과 최소 길이 지정
    note: str = Field(..., min_length=2)    # ...은 기본값이 필요없음, 다른 타입의 대안으로 사용

thing = Creature(
    name="Lee",
    age=25,
    job=["Developler", "Designer"],
    note="go"
)

print(thing.name)
