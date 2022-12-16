"""

"""


from pydantic import BaseModel
from typing import List, Optional
from models.basemodule import Base

class Character(Base):
    name : str
    height: str
    mass: str
    hair_colour: str
    skin_colour: str
    eye_colour: str
    birth_year: str
    gender : str
    homeworld: str
    species: Optional[List[str]]
    starship: Optional[List[str]]
    films: Optional[List[str]]
    vehicles:Optional[List[str]]


