from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

objave = []


class NovaObjava(BaseModel):
    korisnik: str = Field(..., max_length=20)
    tekst: str = Field(..., max_length=280)
    vrijeme: datetime


class Objava(NovaObjava):
    id: int


@app.post("/objava", response_model=Objava, status_code=201)
def kreiraj_objavu(nova_objava: NovaObjava):
    novi_id = 1
    if objave:
        novi_id = objave[-1]["id"] + 1

    objava_dict = nova_objava.model_dump()
    objava_dict["id"] = novi_id

    objave.append(objava_dict)
    return objava_dict


@app.get("/objava/{id}", response_model=Objava)
def dohvati_objavu(id: int):
    for objava in objave:
        if objava["id"] == id:
            return objava

    raise HTTPException(status_code=404, detail="Objava nije pronađena!")


@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
def objave_korisnika(korisnik: str):
    filtrirane_objave = [o for o in objave if o["korisnik"] == korisnik]
    return filtrirane_objave
