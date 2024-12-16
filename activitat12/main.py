from fastapi import FastAPI

from CRUDpantallaprincipal.deletepantallaprincipal import deletepantallap
from CRUDpantallaprincipal.getinfopantallap import getPantallaprincipalcrud
from CRUDpantallaprincipal.postpprincipal import postpantallaprincipalcrud
from CRUDpantallaprincipal.putpantallaprincipal import putpantallap
from CRUDparaules.cruddeleteparaula import crudparauladelete
from CRUDparaules.crudgetparaules import getParaulesss
from CRUDparaules.crudpostparaula import postcrudparaula
from CRUDparaules.crudputparaula import putcrudparaula
from CRUDregistrejoc.crudregistrejoc import getregistredeljoc
from CRUDusuaris.cruddeleteusuari import crudusuaridelete
from CRUDusuaris.crudgetpenjatusuaris import getcrudUsuarisPenjat
from CRUDusuaris.crudpostusuari import postusuari
from conn import getConn
from schemas.crudregistreschema import registreschemas
from schemas.pantallaschemap import pantallaprincipalschemas
from schemas.paraulesschema import paraulesgetschemas
from schemas.usuarisschema import usuarisschemas1

app = FastAPI()

connexio = getConn()

######Paraules
@app.get("/penjat/getparaules/",response_model=list[dict])
async def getParaules():
    return paraulesgetschemas(getParaulesss(connexio))

@app.post("/penjat/postparaules/")
async def postParaules(parauladisplayinicial,parauladisplayactual,paraulasecreta,idjugador,idioma):
    return postcrudparaula(connexio,parauladisplayinicial,parauladisplayactual,paraulasecreta,idjugador,idioma)

@app.put("/penjat/putparaules")
async def putParaules(parauladisplayactual,idjugador):
    return putcrudparaula(connexio,parauladisplayactual,idjugador)

@app.delete("/penjat/deleteparaules")
async def deleteParaules(idjugador):
    return crudparauladelete(connexio,idjugador)

###Pantalla principal
@app.get("/penjat/getpantallaprincipal",response_model=list[dict])
async def getPantallaprincipal():
    return pantallaprincipalschemas(getPantallaprincipalcrud(connexio))

@app.post("/penjat/postpantallaprincipal")
async def postpantalla(idioma,comencarpartidabutton,lletrasabecedari):
    return postpantallaprincipalcrud(connexio,idioma,comencarpartidabutton,lletrasabecedari)

@app.put("/penjat/putpantallaprincipal")
async def updatepantallaprincipal(idioma,comencarpartidabutton):
    return putpantallap(connexio,idioma,comencarpartidabutton)

@app.delete("/penjat/deletepantallaprincipal")
async def deletepantallaprincipal(idioma):
    return deletepantallap(connexio,idioma)

####Usuaris
@app.get("/penjat/getusuaris",response_model=dict)
async def getpenjatUsuaris():
    return usuarisschemas1(getcrudUsuarisPenjat(connexio))

@app.post("/penjat/postusuaris")
async def insertusuaripenjat(idjugador,nomjugador,numerojugades,puntspartidaactual,totalpartides,partidaambmespunts):
    return postusuari(connexio,idjugador,nomjugador,numerojugades,puntspartidaactual,totalpartides,partidaambmespunts)

'''
El de actualitzar els usuaris del penjat ja esta fet a la activitat 11 com a un metode que es diu actualitzar estadistiques.
'''

@app.delete("/penjat/deleteusuaris")
async def deleteusuari(idjugador):
    return crudusuaridelete(connexio,idjugador)

####Registre Joc
@app.get("/penjat/getregistrejoc",response_model=dict)
async def getregistrejoc():
    registreschemas(getregistredeljoc(connexio))

@app.post("/penjat/postregistrejoc")
async def postregisrejoc(idioma):
    return pass

@app.put("/penjat/putregistrejoc")
async def putregistrejoc(idioma):
    return pass

@app.delete("/penjat/deleteregistrejoc")
async def deleteregistrejoc(idioma):
    return pass