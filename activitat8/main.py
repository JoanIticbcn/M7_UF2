from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Usuari(BaseModel):
    nom: str
    cognom: str | None = None
    salari: float
    edat: int | None = None

app = FastAPI()

@app.get("/usuaris/{nom}")
async def get_usuari(nom:str,cognom:str,salari:float,edat:int,):
    usuari = {"nom":nom,"cognom":cognom,"salari":salari,"edat":edat}
    if usuari and nom=="":
        raise HTTPException(status_code=404, detail="Usuari no trobat")
    return usuari

@app.post("/usuaris/")
async def crea_usuari(usuari: Usuari):
    return usuari