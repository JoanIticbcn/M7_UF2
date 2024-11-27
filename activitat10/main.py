from fastapi import FastAPI

from conn import getConn
from read.readOptions import readOptions
from read.readWord import readWord
from schemas import optionsSchema
from schemas import wordSchema

app = FastAPI()

@app.get("/penjat/tematica/opcions",response_model=list[dict])
async def opcionsTematica():
    return optionsSchema.optionsSchema(readOptions(getConn()))

@app.get("/penjat/tematica/{opcion}",response_model=list[dict])
async def getWord(opcion:str):
    return wordSchema.wordSchema(readWord(getConn(),opcion))