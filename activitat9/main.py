from fastapi import FastAPI
from pydantic import BaseModel

from crud import read
from db_connect.conn import getConn
from schemas import users_sch

app = FastAPI()

@app.get("/users",response_model=list[dict])
async def read_users():
    return users_sch.users_schema(read.read_usuaris(getConn()))