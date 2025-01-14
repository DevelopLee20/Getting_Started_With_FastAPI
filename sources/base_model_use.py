from pydantic import BaseModel

class Creature(BaseModel):  # BaseModel 상속
    name: str
    country: str
    area: str

thing = Creature(
    name="Lee",
    country="South Korea",
    area="Anseong"
)

print(thing.name)
