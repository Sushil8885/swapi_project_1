from typing import List, Optional
from models.basemodule import Base


class Planets(Base):
    climate: str
    diameter: str
    films: Optional[List[str]]
    gravity: str
    name: str
    orbital_period: str
    population: str
    residents: Optional[List[str]]
    rotation_period: str
    surface_water: str
    terrain: str


if __name__ == "__main__":
    data = {

        "name": "Tatooine",
        "rotation_period": "23",
        "orbital_period": "304",
        "diameter": "10465",
        "climate": "arid",
        "gravity": "1 standard",
        "terrain": "desert",
        "surface_water": "1",
        "population": "200000",
        "residents": [
            "https://swapi.dev/api/people/1/",
            "https://swapi.dev/api/people/2/",
            "https://swapi.dev/api/people/4/",
            "https://swapi.dev/api/people/6/",
            "https://swapi.dev/api/people/7/",
            "https://swapi.dev/api/people/8/",
            "https://swapi.dev/api/people/9/",
            "https://swapi.dev/api/people/11/",
            "https://swapi.dev/api/people/43/",
            "https://swapi.dev/api/people/62/"
        ],
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/4/",
            "https://swapi.dev/api/films/5/",
            "https://swapi.dev/api/films/6/"
        ],
        "created": "2014-12-09T13:50:49.641000Z",
        "edited": "2014-12-20T20:58:18.411000Z",
        "url": "https://swapi.dev/api/planets/1/"

    }
    obj = Planets(**data)
    print(obj)
    print("###" * 20)
    print(obj.name)
    print("###" * 20)
    print(obj.rotation_period)
    print("###" * 20)
    print(obj.orbital_period)
    print("###" * 20)
    print(obj.diameter)
    print("###" * 20)
    print(obj.terrain)
