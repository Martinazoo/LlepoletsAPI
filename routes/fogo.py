from fastapi import APIRouter
from config.database import conn
from models.models import fogons, users
from schemas.schemas import Fogo, FogoByUsername
from typing import List
fogo = APIRouter()

@fogo.get("/fogons/{username}", response_model=List[Fogo])
def get_fogons_by_username(username: str):
    id_user = conn.execute(users.select().where(users.c.username == username)).first().id
    return conn.execute(fogons.select().where(fogons.c.owner_id == id_user)).fetchall()

@fogo.post("/fogons", response_model=Fogo)
def create_fogo(fogo: FogoByUsername):
    new_fogo = {"title": fogo.title, "power": fogo.power}
    new_fogo["owner_id"] = conn.execute(users.select().where(users.c.username == fogo.username)).first().id
    result = conn.execute(fogons.insert().values(new_fogo))
    conn.execute(users.update().values(num_fogons = users.c.num_fogons + 1).where(users.c.username == fogo.username))
    conn.commit()
    return conn.execute(fogons.select().where(fogons.c.id == result.lastrowid)).first()