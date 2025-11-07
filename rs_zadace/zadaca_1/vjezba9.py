lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def ukloni_duplikate(lista):
    skup = set()  # Pomoćni skup - prazno na početku
    rezultat = []   # Nova lista bez duplikata

    for element in lista:
        if element not in skup:  # Ako ga nismo vidjeli
            skup.add(element)     # Dodaj u skup
            rezultat.append(element)  # Dodaj u rezultat

    return rezultat


print(ukloni_duplikate(lista))
