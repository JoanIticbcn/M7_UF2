from fastapi import FastAPI

from conn import getConn

app = FastAPI()

connexio = getConn()

######Paraules
@app.get("/penjat/btnComençar/{idioma}",response_model=dict)
async def getBtnComensar(idioma):
    return schemabuttontext(textbtn.getbuttontext(connexio,idioma))

@app.post("/penjat/btnComençar/{idioma}",response_model=dict)
async def getBtnComensar(idioma):
    return schemabuttontext(textbtn.getbuttontext(connexio,idioma))

@app.put("/penjat/btnComençar/{idioma}",response_model=dict)
async def getBtnComensar(idioma):
    return schemabuttontext(textbtn.getbuttontext(connexio,idioma))

@app.delete("/penjat/btnComençar/{idioma}",response_model=dict)
async def getBtnComensar(idioma):
    return schemabuttontext(textbtn.getbuttontext(connexio,idioma))