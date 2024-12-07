from fastapi import APIRouter
from config.database import conn
from models.models import users
from schemas.schemas import User, UserLogin, UserRegister
import bcrypt
from typing import List

user = APIRouter()


@user.get("/users", response_model=List[User])
def get_users():
    res_users = conn.execute(users.select().order_by(users.c.num_fogons.desc())).fetchall()    
    if res_users:
        return res_users
    else :
        return {"error": "No users found"}

@user.post("/users", response_model=User)
def create_user(user: UserRegister):
    new_user = {"name": user.name, "username": user.username, "email": user.email}
    new_user["password"] = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

# Aquesta funció funciona quan es posa la contraseña correcta
@user.post("/users/login", response_model=User)
def login_user(user: UserLogin):
    user_db = conn.execute(users.select().where(users.c.username == user.username)).first()
    if user_db:
        if bcrypt.checkpw(user.password.encode('utf-8'),user_db.password.encode('utf-8')):
            print("Contrasenya correcta")
            return user_db
        else :      
            print("Contrasenya incorrecta")   
            return {"error": "Invalid credentials"}


@user.get("/users/{username}", response_model=User)
def get_user_by_username(username: str):
    res = conn.execute(users.select().where(users.c.username == username)).first()
    if res:
        return res
    else:
        return {"error": "User not found"}
    
@user.get("/users/top/", response_model=List[User])
def get_top_users():
    res_users = conn.execute(users.select().order_by(users.c.num_fogons.desc()).limit(3)).fetchall()  
    if res_users:
        return res_users
    else :
        return {"error": "No users found"}