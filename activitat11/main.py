from fastapi import FastAPI

from conn import getConn
from crud import textbtn, textdisplayinicial, postintent, estadistiquesjoc, updateEstadisticas
from schemas.schemaabc import abcschema
from schemas.schematextinicial import schemainitialtext
from schemas.textbtnschema import schemabuttontext

app = FastAPI()

connexio = getConn()

@app.get("/penjat/btnComençar/{idioma}",response_model=dict)
async def getBtnComensar(idioma):
    return schemabuttontext(textbtn.getbuttontext(idioma,connexio))

@app.get("/penjat/paraulaInicial/{idioma}",response_model=dict)
async def getParaulaComensar(idioma):
    return schemainitialtext(textdisplayinicial.gettextinicial(idioma,connexio))

@app.post("/penjat/intents/")
async def postIntent(numerointent,estatpartida,encertada,fallada,lletrautilitzada):
    return postintent.postintentmethod(connexio,numerointent,estatpartida,encertada,fallada,lletrautilitzada)

@app.get("/penjat/abecedari/{idioma}",response_model=list[dict])
async def getAbecedari(idioma):
    return abcschema(getAbecedari(idioma,connexio))

@app.get("/penjat/estadistiques/{nom}",response_model=list)
async def getEstadistiques(nom):
    return estadistiquesjoc.getEstadistiquesdeljoc(connexio,nom)

@app.put("/penjat/estadistiques/")
async def actualitzarEstadistiques(nomjugador,puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts):
    return updateEstadisticas.updateestadisticasdeljoc(connexio,nomjugador,puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts)