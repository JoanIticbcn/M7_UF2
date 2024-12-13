from fastapi import FastAPI

from CRUDpantallaprincipal.deletepantallaprincipal import deletepantallap
from CRUDpantallaprincipal.getinfopantallap import getPantallaprincipalcrud
from CRUDpantallaprincipal.postpprincipal import postpantallaprincipalcrud
from CRUDpantallaprincipal.putpantallaprincipal import putpantallap
from CRUDparaules.cruddeleteparaula import crudparauladelete
from CRUDparaules.crudgetparaules import getParaulesss
from CRUDparaules.crudpostparaula import postcrudparaula
from CRUDparaules.crudputparaula import putcrudparaula
from conn import getConn
from schemas.pantallaschemap import pantallaprincipalschemas
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
    return putcrudparaula(connexio,parauladisplayactual,idjugador)

@app.delete("/penjat/paraules")
async def deleteParaules(idjugador):
    return crudparauladelete(connexio,idjugador)

###Pantalla principal
@app.get("/penjat/pantallaprincipal",response_model=dict)
async def getPantallaprincipal():
    return pantallaprincipalschemas(getPantallaprincipalcrud(connexio))

@app.post("/penjat/pantallaprincipal")
async def postpantalla(idioma,comencarpartidabutton,lletrasabecedari):
    return postpantallaprincipalcrud(connexio,idioma,comencarpartidabutton,lletrasabecedari)

@app.put("/penjat/pantallaprincipal")
async def updatepantallaprincipal(idioma,comencarpartidabutton):
    return putpantallap(connexio,idioma,comencarpartidabutton)

@app.delete("/penjat/pantallaprincipal")
async def deletepantallaprincipal(idioma):
    return deletepantallap(connexio,idioma)

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