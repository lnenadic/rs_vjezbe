import re
from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from models.film import Film

router = APIRouter(prefix="/filmovi", tags=["filmovi"])

filmovi_baza: list[Film] = []


def preprocess_film_data(film_data: dict) -> dict:
    processed = film_data.copy()

    year_str = str(processed.get("Year", ""))
    year_match = re.search(r"(\d{4})", year_str)
    if year_match:
        processed["Year"] = int(year_match.group(1))
    else:
        processed["Year"] = 2000

    runtime_str = str(processed.get("Runtime", "0"))
    runtime_match = re.search(r"(\d+)", runtime_str)
    if runtime_match:
        processed["Runtime"] = int(runtime_match.group(1))
    else:
        processed["Runtime"] = 1

    rating_str = str(processed.get("imdbRating", "N/A"))
    if rating_str not in ["N/A", "", "None"]:
        try:
            processed["imdbRating"] = float(rating_str)
        except ValueError:
            processed["imdbRating"] = None
    else:
        processed["imdbRating"] = None

    votes_str = str(processed.get("imdbVotes", "N/A"))
    if votes_str not in ["N/A", "", "None"]:
        try:
            votes_clean = votes_str.replace(",", "")
            processed["imdbVotes"] = int(votes_clean)
        except ValueError:
            processed["imdbVotes"] = None
    else:
        processed["imdbVotes"] = None

    if processed.get("Type") not in ["movie", "series"]:
        processed["Type"] = "movie"

    if "Images" not in processed or not isinstance(processed["Images"], list):
        processed["Images"] = []

    return processed


def ucitaj_filmove(filmovi_data: list[dict]):
    global filmovi_baza
    filmovi_baza = []
    uspjesno = 0
    neuspjesno = 0

    for film_data in filmovi_data:
        try:
            processed_data = preprocess_film_data(film_data)

            film = Film(**processed_data)
            filmovi_baza.append(film)
            uspjesno += 1

        except Exception as e:
            neuspjesno += 1
            print(
                f"Greška pri učitavanju filma '{film_data.get('Title', 'Unknown')}': {e}"
            )

    print(f"Učitano {uspjesno} filmova u bazu!")
    if neuspjesno > 0:
        print(f"{neuspjesno} filmova nije učitano zbog grešaka u podacima!")


@router.get("/", response_model=list[Film])
async def dohvati_sve_filmove(
    min_year: Optional[int] = Query(None, ge=1900, description="Minimalna godina"),
    max_year: Optional[int] = Query(None, le=2100, description="Maksimalna godina"),
    min_rating: Optional[float] = Query(
        None, ge=0.0, le=10.0, description="Minimalna IMDB ocjena"
    ),
    max_rating: Optional[float] = Query(
        None, ge=0.0, le=10.0, description="Maksimalna IMDB ocjena"
    ),
    type: Optional[str] = Query(None, description="Tip: movie ili series"),
):
    rezultat = filmovi_baza.copy()

    if min_year is not None:
        rezultat = [f for f in rezultat if f.Year >= min_year]

    if max_year is not None:
        rezultat = [f for f in rezultat if f.Year <= max_year]

    if min_rating is not None:
        rezultat = [
            f
            for f in rezultat
            if f.imdbRating is not None and f.imdbRating >= min_rating
        ]

    if max_rating is not None:
        rezultat = [
            f
            for f in rezultat
            if f.imdbRating is not None and f.imdbRating <= max_rating
        ]

    if type is not None:
        rezultat = [f for f in rezultat if f.Type == type]

    return rezultat


@router.get("/imdb/{imdb_id}", response_model=Film)
async def dohvati_film_po_imdb(imdb_id: str):
    for film in filmovi_baza:
        if film.imdbID == imdb_id:
            return film

    raise HTTPException(
        status_code=404, detail=f"Film s IMDB ID-om '{imdb_id}' nije pronađen u bazi"
    )


@router.get("/naslov/{title}", response_model=Film)
async def dohvati_film_po_naslovu(title: str):
    title_lower = title.lower()

    for film in filmovi_baza:
        if film.Title.lower() == title_lower:
            return film

    raise HTTPException(
        status_code=404, detail=f"Film s naslovom '{title}' nije pronađen u bazi"
    )


@router.get("/statistika")
async def dohvati_statistiku():
    if not filmovi_baza:
        return {"ukupno_filmova": 0, "poruka": "Nema filmova u bazi"}

    filmovi_count = sum(1 for f in filmovi_baza if f.Type == "movie")
    serije_count = sum(1 for f in filmovi_baza if f.Type == "series")

    filmovi_s_ocjenom = [f for f in filmovi_baza if f.imdbRating is not None]
    prosjecna_ocjena = None
    if filmovi_s_ocjenom:
        prosjecna_ocjena = round(
            sum(f.imdbRating for f in filmovi_s_ocjenom) / len(filmovi_s_ocjenom), 2
        )

    godine = [f.Year for f in filmovi_baza]

    return {
        "ukupno_filmova": len(filmovi_baza),
        "filmovi": filmovi_count,
        "serije": serije_count,
        "prosjecna_ocjena": prosjecna_ocjena,
        "najstariji_film": min(godine) if godine else None,
        "najnoviji_film": max(godine) if godine else None,
        "filmova_s_ocjenom": len(filmovi_s_ocjenom),
    }


@router.get("/pretraga", response_model=list[Film])
async def pretrazi_filmove(
    glumac: Optional[str] = Query(
        None, description="Pretraži po glumcu (ime ili prezime)"
    ),
    zanr: Optional[str] = Query(None, description="Pretraži po žanru"),
    keyword: Optional[str] = Query(
        None, description="Pretraži po ključnoj riječi u naslovu ili opisu"
    ),
):
    if not glumac and not zanr and not keyword:
        return filmovi_baza

    rezultat = filmovi_baza.copy()

    # Filtriranje - svaki kriterij se primjenjuje na rezultat (AND logika)
    if glumac:
        glumac_lower = glumac.lower()
        rezultat = [f for f in rezultat if glumac_lower in f.Actors.lower()]

    if zanr:
        zanr_lower = zanr.lower()
        rezultat = [f for f in rezultat if zanr_lower in f.Genre.lower()]

    if keyword:
        keyword_lower = keyword.lower()
        rezultat = [
            f
            for f in rezultat
            if keyword_lower in f.Title.lower() or keyword_lower in f.Plot.lower()
        ]

    if not rezultat:
        raise HTTPException(
            status_code=404, detail="Nema filmova koji odgovaraju kriterijima pretrage"
        )

    return rezultat
