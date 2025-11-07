lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def grupiraj_po_paritetu(lista):
    parni = []
    neparni = []
    for broj in lista:
        if broj % 2 == 0:
            parni.append(broj)
        else:
            neparni.append(broj)
    return {'parni': parni, 'neparni': neparni}


print(grupiraj_po_paritetu(lista))
