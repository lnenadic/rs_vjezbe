import math

parni_kvadrati = [x**2 for x in range(20, 51) if x % 2 == 0]
print(parni_kvadrati)
print("------------")

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if 'a' in rijec]
print(duljine_sa_slovom_a)
print("------------")

kubovi = [{x: x**3} if x % 2 != 0 else {x: x} for x in range(1, 11)]
print(kubovi)   
print("------------")

korijeni = {x: round(x**0.5, 2) for x in range(50, 501, 50)}
print(korijeni)
print("------------")

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [{student["prezime"]: sum(student["bodovi"])} for student in studenti]
print(zbrojeni_bodovi)
print("------------")

faktorijeli = {x: [math.factorial(i) for i in range(1, x + 1)] for x in range(1, 11)}
print(faktorijeli)