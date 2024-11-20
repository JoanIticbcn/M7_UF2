from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Arxiu de proves per a fer proves dels 4 primers apartats
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []


@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results