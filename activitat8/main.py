from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Missatge": "Fast API de Joan","Versio":"En proves","Data":"11/11/2024"}

@app.post("/post/{edat}")
async def post(edat:int):
    return {"La teva edat es":edat}