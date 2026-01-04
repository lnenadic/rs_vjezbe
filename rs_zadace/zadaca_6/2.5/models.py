from ast import List
from datetime import datetime
from decimal import Decimal
from typing import Literal, TypedDict

from click import Tuple
from pydantic import BaseModel, Field


# --- 1. ---
class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdanja: int = datetime.now().year
    broj_stranica: int
    izdavac: Izdavac


class Izdavac(BaseModel):
    naziv: str
    adresa: str


# --- 2. ---
Ovlasti = Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]


class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: Literal[Ovlasti] = Field(default_factory=list)


# --- 3. ---
class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float


class StolInfo(TypedDict):
    broj: int
    lokacija: str


class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: List[Jelo]
    ukupna_cijena: float


# --- 4. ---
class CCTVFrame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: Tuple[Decimal, Decimal] = Field(
        default=(Decimal("0.0"), Decimal("0.0"))
    )
