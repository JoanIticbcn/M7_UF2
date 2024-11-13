from fastapi import FastAPI, Response
from pydantic import BaseModel

class Usuari(BaseModel):
    nom: str
    cognom: str | None = None
    salari: float
    edat: int | None = None

app = FastAPI()

@app.get("/usuaris/{nom}")
async def get_usuari(nom:str,cognom:str,salari:float,edat:int,response:Response):
    usuari = {"nom":nom,"cognom":cognom,"salari":salari,"edat":edat}
    if usuari and nom=="":
        response.status_code = 404
        return {"Error":"Usuari no trobat"}
    return usuari

@app.post("/usuaris/")
async def crea_usuari(usuari: Usuari):
    return usuari