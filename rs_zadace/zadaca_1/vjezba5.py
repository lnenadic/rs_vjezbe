for i in range(1, 2):
    print(i)
# Nema smisla jer petlja se izvršava samo jednom. U ovom slučaju bolje je koristiti print(1).

for i in range(10, 1, 2):
    print(i)
# Petlja se neće izvržiti, potrebno je za step koristiti negativnu vrijednost(npr. -2).

for i in range(10, 1, -1):
    print(i)
""
10
9
8
7
6
5
4
3
2
# Program ispravno ispisuje brojeve od 10 do 2 unazad, korak je -1.
""
