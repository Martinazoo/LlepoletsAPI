from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routes.user import user    
from routes.fogo import fogo

app = FastAPI()
app.include_router(user)
app.include_router(fogo)