from pydantic import BaseModel
from typing import List

class Fogons(BaseModel):
    id: int
    title: str
    description: str
    power: int

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    password: str
    image: str
    numFires: List[Fogons]

