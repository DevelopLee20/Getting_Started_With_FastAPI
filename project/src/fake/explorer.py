from model.explorer import Explorer

_explorers = [
    Explorer(
        name="one",
        country="KR",
        description="one des"
    ),
    Explorer(
        name="two",
        country="JP",
        description="two des"
    ),
]

def get_all() -> list[Explorer]:
    """탐험가 목록 반환"""
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    
    return None

def create(explorer: Explorer) -> Explorer:
    return explorer

def modify(name: str, explorer: Explorer) -> Explorer:
    return explorer

def replace(name: str, explorer: Explorer) -> Explorer:
    return explorer
