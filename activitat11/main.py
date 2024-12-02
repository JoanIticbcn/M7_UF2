from fastapi import FastAPI

from conn import getConn

app = FastAPI()

connexio = getConn()

@app.get("/penjat/btnComençar/{idioma}",response_model=str)
async def getBtnComensar(idioma):
    return ""

@app.get("/penjat/paraulaInicial/{idioma}",response_model=str)
async def getParaulaComensar(idioma):
    return ""

@app.post("/penjat/intents")
async def postIntent():
    return ""

@app.get("/penjat/abecedari/{idioma}",response_model=list)
async def getAbecedari(idioma):
    return ""