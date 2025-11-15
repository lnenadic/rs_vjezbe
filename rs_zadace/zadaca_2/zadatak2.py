nizovi = ["jabuka", "kruška", "banana", "naranča"]

kvadriraj_duljinu = list(map(lambda niz: len(niz) ** 2, nizovi))

print(kvadriraj_duljinu)
print("-------------------")

brojevi_1 = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

veci_od_5 = list(filter(lambda broj: broj > 5, brojevi_1))

print(veci_od_5)
print("-------------------")

brojevi_2 = [10, 5, 12, 15, 20]

transform = dict(map(lambda broj: (broj, broj ** 2), brojevi_2))

print(transform)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni = all(map(lambda student: student["godine"] >= 18, studenti))

print(svi_punoljetni)
print("-------------------")

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

min_duljina = input("Unesite minimalnu duljinu riječi: ")

duge_rijeci = list(filter(lambda rijec: len(rijec) >= int(min_duljina), rijeci))

print(duge_rijeci)