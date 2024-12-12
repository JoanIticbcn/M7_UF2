from fastapi import FastAPI

from CRUDparaules.cruddeleteparaula import crudparauladelete
from CRUDparaules.crudgetparaules import getParaulesss
from CRUDparaules.crudpostparaula import postcrudparaula
from conn import getConn
from schemas.paraulesschema import paraulesgetschemas

app = FastAPI()

connexio = getConn()

######Paraules
@app.get("/penjat/paraules/",response_model=list[dict])
async def getParaules():
    return paraulesgetschemas(getParaulesss(connexio))

@app.post("/penjat/paraules/")
async def postParaules(parauladisplayinicial,parauladisplayactual,paraulasecreta,idjugador,idioma):
    return postcrudparaula(connexio,parauladisplayinicial,parauladisplayactual,paraulasecreta,idjugador,idioma)

@app.put("/penjat/paraules")
async def putParaules(parauladisplayactual,idjugador):
    return postcrudparaula(connexio,parauladisplayactual,idjugador)

@app.delete("/penjat/paraules")
async def deleteParaules(idjugador):
    return crudparauladelete(connexio,idjugador)

###Pantalla principal
@app.get("/penjat/pantallaprincipal",response_model=dict)
async def getBtnComensar(idioma):
    return pass

@app.post("/penjat/pantallaprincipal")
async def getBtnComensar(idioma):
    return pass

@app.put("/penjat/pantallaprincipal")
async def getBtnComensar(idioma):
    return pass

@app.delete("/penjat/pantallaprincipal")
async def getBtnComensar(idioma):
    return pass

####Usuaris
@app.get("/penjat/usuaris",response_model=dict)
async def getBtnComensar(idioma):
    return pass

@app.post("/penjat/usuaris")
async def getBtnComensar(idioma):
    return pass

@app.put("/penjat/usuaris")
async def getBtnComensar(idioma):
    return pass

@app.delete("/penjat/usuaris")
async def getBtnComensar(idioma):
    return pass

####Registre Joc
@app.get("/penjat/registrejoc",response_model=dict)
async def getBtnComensar(idioma):
    return pass

@app.post("/penjat/registrejoc")
async def getBtnComensar(idioma):
    return pass

@app.put("/penjat/registrejoc")
async def getBtnComensar(idioma):
    return pass

@app.delete("/penjat/registrejoc")
async def getBtnComensar(idioma):
    return pass