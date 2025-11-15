from shop import proizvodi
from shop import narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

def dodaj_proizvode(proizvodi_za_dodavanje, skladiste):
    for proizvod in proizvodi_za_dodavanje:
        novi_proizvod = proizvodi.Proizvod(
            proizvod["naziv"], 
            proizvod["cijena"], 
            proizvod["dostupna_kolicina"]
        )
        proizvodi.dodaj_proizvod(novi_proizvod, skladiste)

dodaj_proizvode(proizvodi_za_dodavanje, proizvodi.skladiste)

for proizvod in proizvodi.skladiste:
    print(proizvod.ispis())

naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}
]

narudzbe.napravi_narudzbu(naruceni_proizvodi, proizvodi.skladiste)