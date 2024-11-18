<h1>Documentació Activitat 9</h1>

<h2>Body field</h2>

<h4>El Field es una propietat que tenen els camps del Base Model.
Amb el Base Model es pot definir un model d'objecte en el que hi ha uns camps especifics que són d'un tipus de dades determinat. El Body Field ens serveix per a afegir informació adicional als camps del nostre Base Model, Afegint-hi constraints, descripcions,valors per defecre(default) o propietats com el max_length o el gt que es greater than 0. Serveix per a fer que el nostre base model sigui el més paregut possible a la estructura de la nostra base de dades.</h4>
<p>--Exemple de codi aplicant algunes caracteristiques del Body Field</p>
<p>from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results</p>

<h4>En el codi podem veure les propietats que he mencionat anteriorment com el gt el title o la description</h4>
<h4>Captures del Postman del codi anterior</h4>
<img src="captures/postmanField.png"></img>
<p>En aquesta captura veiem que el codi falla per 2 motius, el primer es perque no hi ha cap registre amb el ID 1 i el segon motiu es perquè el price hem posat -1 i el field tenia una condició que el price havia de ser més gran que 0 llavors el programa peta. Es un comportament similar a les constraints de les bases de dades que ens va enseñar el Jordi Quesada.</p>