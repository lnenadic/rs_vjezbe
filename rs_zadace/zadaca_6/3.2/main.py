from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from models import Automobil, CarCreate

app = FastAPI()

automobili = [
    {
        "id": 1,
        "marka": "Toyota",
        "model": "RAV4",
        "godina_proizvodnje": 2015,
        "cijena": 18000.0,
        "boja": "siva",
    },
    {
        "id": 2,
        "marka": "Seat",
        "model": "Leon",
        "godina_proizvodnje": 2020,
        "cijena": 20000.0,
        "boja": "bijela",
    },
    {
        "id": 3,
        "marka": "Ford",
        "model": "Focus",
        "godina_proizvodnje": 2012,
        "cijena": 12000.0,
        "boja": "crvena",
    },
]

PDV_STOPA = 0.25


@app.get("/automobili/{automobil_id}", response_model=Automobil)
def get_automobil(
    automobil_id: int,
    min_cijena: Optional[float] = Query(None, gt=0),
    max_cijena: Optional[float] = Query(None),
    min_godina: Optional[int] = Query(None, gt=1960),
    max_godina: Optional[int] = Query(None),
):
    if min_cijena is not None and max_cijena is not None and min_cijena > max_cijena:
        raise HTTPException(
            status_code=400,
            detail="Minimalna cijena ne smije biti veća od maksimalne cijene",
        )

    if min_godina is not None and max_godina is not None and min_godina > max_godina:
        raise HTTPException(
            status_code=400,
            detail="Minimalna godina ne smije biti veća od maksimalne godine",
        )

    automobil = None
    for auto in automobili:
        if auto["id"] == automobil_id:
            automobil = auto
            break

    if automobil is None:
        raise HTTPException(status_code=404, detail="Automobil nije pronađen")

    if min_cijena is not None and automobil["cijena"] < min_cijena:
        raise HTTPException(
            status_code=404, detail="Automobil ne zadovoljava uvjete cijene"
        )

    if max_cijena is not None and automobil["cijena"] > max_cijena:
        raise HTTPException(
            status_code=404, detail="Automobil ne zadovoljava uvjete cijene"
        )

    if min_godina is not None and automobil["godina_proizvodnje"] < min_godina:
        raise HTTPException(
            status_code=404, detail="Automobil ne zadovoljava uvjete godine"
        )

    if max_godina is not None and automobil["godina_proizvodnje"] > max_godina:
        raise HTTPException(
            status_code=404, detail="Automobil ne zadovoljava uvjete godine"
        )

    return automobil


@app.post("/automobili", response_model=Automobil)
def add_automobil(novi_auto: CarCreate):
    for auto in automobili:
        if (
            auto["marka"] == novi_auto.marka
            and auto["model"] == novi_auto.model
            and auto["godina_proizvodnje"] == novi_auto.godina_proizvodnje
        ):
            raise HTTPException(
                status_code=400,
                detail="Automobil već postoji u bazi podataka",
            )

    novi_id = max(auto["id"] for auto in automobili) + 1

    cijena_pdv = novi_auto.cijena * (1 + PDV_STOPA)

    automobil = {
        "id": novi_id,
        "marka": novi_auto.marka,
        "model": novi_auto.model,
        "godina_proizvodnje": novi_auto.godina_proizvodnje,
        "cijena": novi_auto.cijena,
        "cijena_pdv": cijena_pdv,
        "boja": novi_auto.boja,
    }

    automobili.append(automobil)
    return automobil
