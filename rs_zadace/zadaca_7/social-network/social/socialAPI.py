from datetime import datetime
from typing import List

import aiohttp
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

objave = [
    {"id": 1, "korisnik": "Lovre", "tekst": "Hello World!", "vrijeme": datetime.now()}
]


class NovaObjava(BaseModel):
    korisnik: str = Field(..., max_length=20)
    tekst: str = Field(..., max_length=280)
    vrijeme: datetime


class Objava(NovaObjava):
    id: int


class AuthPodaci(BaseModel):
    korisnicko_ime: str
    lozinka: str


@app.post("/objava", response_model=Objava, status_code=201)
def kreiraj_objavu(nova_objava: NovaObjava):
    novi_id = 1 if not objave else objave[-1]["id"] + 1
    objava_dict = nova_objava.model_dump()
    objava_dict["id"] = novi_id
    objave.append(objava_dict)
    return objava_dict


@app.get("/objava/{id}", response_model=Objava)
def dohvati_objavu(id: int):
    for objava in objave:
        if objava["id"] == id:
            return objava
    raise HTTPException(status_code=404, detail="Nije pronađena!")


@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
async def objave_korisnika(
    korisnik: str,
    auth_data: AuthPodaci = Body(...),
):
    login_payload = {
        "korisnicko_ime": auth_data.korisnicko_ime,
        "lozinka": auth_data.lozinka,
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                "http://authapi:9000/login", json=login_payload
            ) as resp:

                if resp.status != 200:
                    raise HTTPException(
                        status_code=401,
                        detail="Neuspješna autorizacija na Auth servisu!",
                    )

        except aiohttp.ClientError:
            raise HTTPException(status_code=503, detail="Auth servis nedostupan!")

    filtrirane = [o for o in objave if o["korisnik"] == korisnik]
    return filtrirane
