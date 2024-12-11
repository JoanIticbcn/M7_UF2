from fastapi import FastAPI

from conn import getConn
from crud import textbtn, textdisplayinicial, postintent, estadistiquesjoc, updateEstadisticas
from crud.lletresabecedari import getabecedaris
from schemas.schematextinicial import schemainitialtext
from schemas.statsschema import statsschemas
from schemas.textbtnschema import schemabuttontext

app = FastAPI()

connexio = getConn()

@app.get("/penjat/btnComençar/{idioma}",response_model=dict)
async def getBtnComensar(idioma):
    print(idioma)
    return schemabuttontext(textbtn.getbuttontext(connexio,idioma))

@app.get("/penjat/paraulaInicial/{idioma}",response_model=dict)
async def getParaulaComensar(idioma):
    return schemainitialtext(textdisplayinicial.gettextinicial(idioma,connexio))

@app.post("/penjat/intents/")
async def postIntent(numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador):
    return postintent.postintentmethod(connexio,numerointent,estatpartida,encertada,fallada,lletrautilitzada,idjugador)

@app.get("/penjat/abecedari/{idioma}",response_model=list)
async def getAbecedari(idioma):
    return getabecedaris(idioma,connexio)

@app.get("/penjat/estadistiques/{nom}",response_model=list)
async def getEstadistiques(nom):
    return statsschemas(estadistiquesjoc.getEstadistiquesdeljoc(connexio,nom))

@app.put("/penjat/estadistiques/")
async def actualitzarEstadistiques(nomjugador,puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts):
    return updateEstadisticas.updateestadisticasdeljoc(connexio,nomjugador,puntspartidaactual,totalpartides,partidesguanyades,partidaambmespunts)