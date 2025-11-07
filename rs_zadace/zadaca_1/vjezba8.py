lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filtriraj_parne(brojevi):
    return [broj for broj in brojevi if broj % 2 == 0]


print(filtriraj_parne(lista))
