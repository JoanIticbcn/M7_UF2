from fastapi import FastAPI

from conn import getConn
from read.readOptions import readOptions
from read.readWord import readWord
from schemas import optionsSchema
from schemas import wordSchema

app = FastAPI()

connexio = getConn()

@app.get("/penjat/tematica/opcions",response_model=list[dict])
async def opcionsTematica():
    return optionsSchema.optionsSchema(readOptions(connexio))

@app.get("/penjat/tematicas/{opcion}",response_model=dict)
async def getWord(opcion:str):
    return wordSchema.wordSchemas(readWord(connexio,opcion))