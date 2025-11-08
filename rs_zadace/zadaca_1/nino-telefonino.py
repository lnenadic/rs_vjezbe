fiksni_brojevi = {
    "01": "Grad Zagreb i Zagrebačka županija",
    "020": "Dubrovačko-neretvanska županija",
    "021": "Splitsko-dalmatinska županija",
    "022": "Šibensko-kninska županija",
    "023": "Zadarska županija",
    "031": "Osječko-baranjska županija",
    "032": "Vukovarsko-srijemska županija",
    "033": "Virovitičko-podravska županija",
    "034": "Požeško-slavonska županija",
    "035": "Brodsko-posavska županija",
    "040": "Međimurska županija",
    "042": "Varaždinska županija",
    "043": "Bjelovarsko-bilogorska županija",
    "044": "Sisačko-moslavačka županija",
    "047": "Karlovačka županija",
    "048": "Koprivničko-križevačka županija",
    "049": "Krapinsko-zagorska županija",
    "051": "Primorsko-goranska županija",
    "052": "Istarska županija",
    "053": "Ličko-senjska županija"
}

mobilni_brojevi = {
    "091": "A1 Hrvatska",
    "092": "Tomato",
    "095": "Telemach",
    "097": "bonbon",
    "098": "Hrvatski Telekom",
    "099": "Hrvatski Telekom"
}

posebne_usluge = {
    "0800": "Besplatni pozivi",
    "060": "Komercijalni pozivi",
    "061": "Glasovanje telefonom",
    "064": "Usluge s neprimjerenim sadržajem",
    "065": "Nagradne igre",
    "069": "Usluge namijenjene djeci",
    "072": "Jedinstveni pristupni broj za cijelu državu za posebne usluge"
}


def ocisti_broj(broj: str):
    broj = broj.replace(" ", "").replace(
        "-", "").replace("(", "").replace(")", "")

    if broj.startswith("+385"):
        broj = broj.replace("+385", "0", 1)
    elif broj.startswith("00385"):
        broj = broj.replace("00385", "0", 1)
    elif broj.startswith("385"):
        broj = broj.replace("385", "0", 1)

    return broj


def prepoznaj_pozivni_broj(ocisceni_broj: str):
    for pozivni in sorted(posebne_usluge.keys(), key=len, reverse=True):
        if ocisceni_broj.startswith(pozivni):
            ostatak = ocisceni_broj[len(pozivni):]
            return (pozivni, ostatak, "posebne usluge", posebne_usluge[pozivni])

    for pozivni in sorted(mobilni_brojevi.keys(), key=len, reverse=True):
        if ocisceni_broj.startswith(pozivni):
            ostatak = ocisceni_broj[len(pozivni):]
            return (pozivni, ostatak, "mobilna mreža", mobilni_brojevi[pozivni])

    for pozivni in sorted(fiksni_brojevi.keys(), key=len, reverse=True):
        if ocisceni_broj.startswith(pozivni):
            ostatak = ocisceni_broj[len(pozivni):]
            return (pozivni, ostatak, "fiksna mreža", fiksni_brojevi[pozivni])

    return (None, ocisceni_broj, None, None)


def validiraj_broj_telefona(broj: str):
    ocisceni_broj = ocisti_broj(broj)
    pozivni, ostatak, vrsta, opis = prepoznaj_pozivni_broj(ocisceni_broj)

    rezultat = {
        "pozivni_broj": pozivni,
        "broj_ostatak": ostatak,
        "vrsta": vrsta,
        "mjesto": None,
        "operater": None,
        "validan": False
    }

    if pozivni is None:
        return rezultat

    if vrsta == "fiksna mreža":
        rezultat["mjesto"] = opis
    elif vrsta == "mobilna mreža":
        rezultat["operater"] = opis

    duljina = len(ostatak)
    if not ostatak.isdigit():
        rezultat["validan"] = False
    elif vrsta in ("fiksna mreža", "mobilna mreža"):
        rezultat["validan"] = duljina in (6, 7)
    elif vrsta == "posebne usluge":
        rezultat["validan"] = duljina == 6

    return rezultat


print("Zadatak: Nino Telefonino - Raspodijeljeni sustavi")
print("")

test_brojevi = [
    "+385 92 741 8520",
    "00385-95-000-4321",
    "091 314 1592",
    "063 123 9876",
    "0800 404 707",
    "12345",
]

for broj in test_brojevi:

    rezultat = validiraj_broj_telefona(broj)

    if rezultat["validan"]:
        print("Broj:", broj, "- je valjan!")
    else:
        print("Broj:", broj, "- nije valjan!")

    print(" Pozivni broj:", rezultat["pozivni_broj"])
    print(" Ostatak broja:", rezultat["broj_ostatak"])
    print(" Vrsta:", rezultat["vrsta"])
    print(" Mjesto:", rezultat["mjesto"])
    print(" Operater:", rezultat["operater"])
    print()
