from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator


class Actor(BaseModel):
    name: str
    surname: str


class Writer(BaseModel):
    name: str
    surname: str


def parse_names_to_objects(names_str: str, model_class):
    if not names_str:
        return []

    result = []
    names_list = [name.strip() for name in names_str.split(",")]

    for full_name in names_list:
        parts = full_name.strip().split()
        if len(parts) >= 2:
            surname = parts[-1]
            name = " ".join(parts[:-1])
            result.append(model_class(name=name, surname=surname))
        elif len(parts) == 1:
            result.append(model_class(name=parts[0], surname=""))

    return result


class Film(BaseModel):
    Title: str = Field(..., description="Naslov filma")
    Year: int = Field(..., description="Godina izdanja (mora biti > 1900)")
    Rated: str = Field(..., description="Ocjena dobne granice (npr. PG-13)")
    Runtime: int = Field(..., description="Trajanje u minutama (mora biti > 0)")
    Genre: str = Field(..., description="Žanr filma")
    Language: str = Field(..., description="Jezik filma")
    Country: str = Field(..., description="Zemlja produkcije")
    Actors: str = Field(..., description="Glumci (imena odvojena zarezom)")
    Plot: str = Field(..., description="Radnja filma")
    Writer: str = Field(..., description="Scenaristi")

    imdbID: Optional[str] = Field(None, description="IMDB identifikator")
    Released: Optional[str] = Field(None, description="Datum izdanja")
    Director: Optional[str] = Field(None, description="Redatelj")
    Awards: Optional[str] = Field(None, description="Nagrade")
    Poster: Optional[str] = Field(None, description="URL postera")
    Metascore: Optional[str] = Field(None, description="Metascore ocjena")
    imdbRating: Optional[float] = Field(None, description="IMDB ocjena (0-10)")
    imdbVotes: Optional[int] = Field(None, description="Broj IMDB glasova (> 0)")
    Type: Literal["movie", "series"] = Field(
        "movie", description="Tip: movie ili series"
    )
    DVD: Optional[str] = Field(None, description="Datum DVD izdanja")
    BoxOffice: Optional[str] = Field(None, description="Zarada")
    Production: Optional[str] = Field(None, description="Produkcijska kuća")
    Website: Optional[str] = Field(None, description="Web stranica")
    Response: Optional[str] = Field(None, description="API odgovor status")
    Images: list[str] = Field(default_factory=list, description="Lista URL-ova slika")

    @field_validator("Year")
    @classmethod
    def validate_year(cls, v):
        if v <= 1900:
            raise ValueError("Godina mora biti veća od 1900")
        return v

    @field_validator("Runtime")
    @classmethod
    def validate_runtime(cls, v):
        if v <= 0:
            raise ValueError("Trajanje filma mora biti veće od 0 minuta")
        return v

    @field_validator("imdbRating")
    @classmethod
    def validate_rating(cls, v):
        if v is not None and (v < 0 or v > 10):
            raise ValueError("IMDB ocjena mora biti između 0 i 10")
        return v

    @field_validator("imdbVotes")
    @classmethod
    def validate_votes(cls, v):
        if v is not None and v < 0:
            raise ValueError("Broj IMDB glasova ne može biti negativan")
        return v

    @field_validator("Images")
    @classmethod
    def validate_images(cls, v):
        if not isinstance(v, list):
            raise ValueError("Images mora biti lista")
        for img in v:
            if not isinstance(img, str):
                raise ValueError("Svaki element u Images mora biti string (URL)")
        return v

    def get_actors_list(self) -> list[Actor]:
        return parse_names_to_objects(self.Actors, Actor)

    def get_writers_list(self) -> list[Writer]:
        return parse_names_to_objects(self.Writer, Writer)

    def get_genres_list(self) -> list[str]:
        return [g.strip() for g in self.Genre.split(",")]

    class Config:
        json_schema_extra = {
            "example": {
                "Title": "Forrest Gump",
                "Year": 1994,
                "Rated": "PG-13",
                "Runtime": 142,
                "Genre": "Drama",
                "Language": "English",
                "Country": "USA",
                "Actors": "Tom Hanks, Robin Wright, Gary Sinise",
                "Plot": "The history of the United States...",
                "Writer": "Winston Groom, Eric Roth",
                "Type": "movie",
                "imdbRating": 8.8,
                "Images": ["https://example.com/image1.jpg"],
            }
        }
