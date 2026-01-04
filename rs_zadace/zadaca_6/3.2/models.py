from pydantic import BaseModel


class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str


class CarCreate(BaseCar):
    pass


class Automobil(BaseCar):
    id: int
    cijena_pdv: float
