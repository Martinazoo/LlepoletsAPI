from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
    id: Optional[int]
    name: str
    username: str
    email: str
    password: str
    num_fogons: Optional[int]
    
class UserRegister(BaseModel):
    name: str
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str
    
class Fogo(BaseModel):
    id: Optional[int]
    title: str
    power: int
    owner_id: int

class FogoByUsername(BaseModel):
    title: str
    power: int
    owner_id: int
    username: str