class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena
        
    def ispis_narudzbe(self):
        proizvodi_tekst = ', '.join(f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi)
        return f"Naručeni proizvodi: {proizvodi_tekst}, Ukupna cijena: {self.ukupna_cijena} eur"

narudzbe = []

def napravi_narudzbu(naruceni_proizvodi, skladiste):
    if not isinstance(naruceni_proizvodi, list):
        print(f"Greška! {naruceni_proizvodi} mora biti lista!") 
        return None
    
    if len(naruceni_proizvodi) == 0:
        print("Greška! Lista proizvoda ne smije biti prazna!")
        return None
    
    for proizvod in naruceni_proizvodi:
        if not isinstance(proizvod, dict):
            print("Greška! Svaki element u listi mora biti rječnik!")
            return None
    
    potrebni_kljucevi = {'naziv', 'cijena', 'narucena_kolicina'}
    for proizvod in naruceni_proizvodi:
        if not potrebni_kljucevi.issubset(proizvod.keys()):
            print(f"Greška! Rječnik mora sadržavati ključeve {potrebni_kljucevi}!")
            return None
    
    for proizvod_dict in naruceni_proizvodi:
        naziv = proizvod_dict['naziv']
        narucena_kolicina = proizvod_dict['narucena_kolicina']
        
        proizvod_na_skladistu = None
        for p in skladiste:
            if p.naziv == naziv:
                proizvod_na_skladistu = p
                break
        
        if proizvod_na_skladistu is None:
            print(f"Proizvod {naziv} nije dostupan!")
            return None
        
        if proizvod_na_skladistu.dostupna_kolicina < narucena_kolicina:
            print(f"Proizvod {naziv} nije dostupan u traženoj količini!")
            return None
    
    ukupna_cijena = sum(p['cijena'] * p['narucena_kolicina'] for p in naruceni_proizvodi)
    
    nova_narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)
    
    narudzbe.append(nova_narudzba)
    
    return nova_narudzba