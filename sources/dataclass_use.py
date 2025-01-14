from dataclasses import dataclass

@dataclass  # 클래스 필드 값 기반 생성자 메서드(__init__)를 자동으로 생성, 기타 유용한 메서드 자동 생성(보일러플레이트 코드)
class CreatureDataClass():
    name: str
    country: str
    area: str

things = CreatureDataClass(
    name="Lee",
    country="South Korea",
    area="Anseong"
)

print(things.name)
