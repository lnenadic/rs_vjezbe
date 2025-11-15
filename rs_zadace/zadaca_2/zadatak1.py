def kvadriraj(x):
    return x ** 2

kvadriraj_l = lambda x: x ** 2

print(kvadriraj(5))
print(kvadriraj_l(5))
print("-------------------")

def zbroji_pa_kvadriraj(a, b):
    return (a + b) ** 2

zbroji_pa_kvadriraj_l = lambda a, b: (a + b) ** 2


print(zbroji_pa_kvadriraj(3, 3))
print(zbroji_pa_kvadriraj_l(3, 3))
print("-------------------")

def kvadriraj_duljinu(niz):
    return len(niz) ** 2

kvadriraj_duljinu_l = lambda niz: len(niz) ** 2

print(kvadriraj_duljinu("Raspodijeleni sustavi"))
print(kvadriraj_duljinu_l("Raspodijeleni sustavi"))
print("-------------------")

def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x

pomnozi_i_potenciraj_l = lambda x, y: (y * 5) ** x

print(pomnozi_i_potenciraj(2, 2))
print(pomnozi_i_potenciraj_l(2, 2))
print("-------------------")

def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return None

pran_broj_l = lambda x: True if x % 2 == 0 else None

print(paran_broj(4))
print(paran_broj(5))
print(pran_broj_l(4))
print(pran_broj_l(5))
