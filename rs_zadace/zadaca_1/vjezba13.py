lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def prvi_i_zadnji(lst):
    return lst[0], lst[-1]


print("1. Funkcija", prvi_i_zadnji(lista))  # (1, 10)


lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]


def maks_i_min(lst):
    maksimum = lst[0]
    minimum = lst[0]

    for broj in lst[1:]:
        if broj > maksimum:
            maksimum = broj

        if broj < minimum:
            minimum = broj

    return (maksimum, minimum)


print("2. Funkcija", maks_i_min(lista))  # (250, 5)


skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}


def presjek(s1, s2):
    rezultat = set()

    for element in s1:
        if element in s2:
            rezultat.add(element)

    return rezultat


print("3. Funkcija", presjek(skup_1, skup_2))
