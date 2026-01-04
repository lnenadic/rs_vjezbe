import json
from contextlib import asynccontextmanager

from fastapi import FastAPI
from routers import filmovi


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with open("movies.json", "r", encoding="utf-8") as f:
            filmovi_data = json.load(f)

        filmovi.ucitaj_filmove(filmovi_data)

    except FileNotFoundError:
        print("Greška: movies.json nije pronađen!")
    except Exception as e:
        print(f"Greška pri učitavanju: {e}")

    yield


app = FastAPI(
    title="Mikroservis za filmove",
    description="Razvoj FastAPI mikroservisa za dohvaćanje podataka o filmovima - RS Vježbe 6",
    version="1.0",
    lifespan=lifespan,
)

app.include_router(filmovi.router)


@app.get("/")
async def root():
    return {"poruka": "Dobrodošli u mikroservis za filmove!", "dokumentacija": "/docs"}
