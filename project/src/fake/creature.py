from model.creature import Creature

_creatures = [
    Creature(
        name="Test1",
        aka="tester1",
        country="CN",
        area="Hima",
        description="test1",
    ),

    Creature(
        name="Test1",
        description="Yes",
        country="KR",
        area="here",
        aka="Sqeust"
    ),
]

def get_all() -> list[Creature]:
    return _creatures

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    
    return None

def create(creature: Creature) -> Creature:
    return creature

def modify(name: str, creature: Creature) -> Creature:
    return creature

def replace(name: str, creature: Creature) -> Creature:
    return creature

def delete(name: str) -> bool:
    for _creature in _creatures:
        if _creature.name == name:
            return True
        
    return False
