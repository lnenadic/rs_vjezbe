from typing import List, Optional

from fastapi import FastAPI, HTTPException
from models import CreateFilm, Film

app = FastAPI()

filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008},
]
next_id = 5


@app.get("/filmovi", response_model=List[Film])
def get_filmovi(genre: Optional[str] = None, min_godina: int = 2000):
    filtrirani_filmovi = filmovi

    if genre is not None:
        filtrirani_filmovi = [
            film
            for film in filtrirani_filmovi
            if film["genre"].lower() == genre.lower()
        ]

    filtrirani_filmovi = [
        film for film in filtrirani_filmovi if film["godina"] >= min_godina
    ]

    return filtrirani_filmovi


@app.get("/filmovi/{id}", response_model=Film)
def get_film_by_id(id: int):
    for film in filmovi:
        if film["id"] == id:
            return film
    raise HTTPException(status_code=404, detail="Film s traženim ID-jem ne postoji!")


@app.post("/filmovi", response_model=Film)
def create_film(film: CreateFilm):
    global next_id

    novi_film = {
        "id": next_id,
        "naziv": film.naziv,
        "genre": film.genre,
        "godina": film.godina,
    }

    filmovi.append(novi_film)
    next_id += 1

    return novi_film
