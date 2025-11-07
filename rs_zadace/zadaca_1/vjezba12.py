rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}


def obrni_rjecnik(rjecnik):
    obrnut_rjecnik = {}
    for kljuc, vrijednost in rjecnik.items():
        obrnut_rjecnik[vrijednost] = kljuc
    return obrnut_rjecnik


print(obrni_rjecnik(rjecnik))
