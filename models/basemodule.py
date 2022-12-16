"""
This module defines a pydantic basemodel to be used another
pydantic models(resource models aka "data models")

"""

from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):
    """ common attributes available in all resources"""

    created: datetime
    edited: datetime
    url: str

if __name__ == "__main__":
    data = {
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/"
    }

    obj = Base(**data)
    print(obj)
    print("***" * 10)
    print(obj.created)
    print(type(obj.created))
    print("***" * 10)
    print(obj.edited)
    print(type(obj.edited))
    print("***" * 10)
    print(obj.url)
    print(type(obj.url))
    print("***" * 10)
