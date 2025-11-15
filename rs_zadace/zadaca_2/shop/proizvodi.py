class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina
    
    def ispis(self):
        return f"Proizvod: {self.naziv}, Cijena: {self.cijena} €, Dostupna količina: {self.dostupna_kolicina}"

skladiste = [
    Proizvod("MacBook Pro 14' M5", 1500, 10),
    Proizvod("iPhone 16 Pro Max", 1100, 50)
]

def dodaj_proizvod(proizvod, skladiste):
    skladiste.append(proizvod)