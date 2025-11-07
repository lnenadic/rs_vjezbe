total_sum = 0

while True:
    number = int(input("Unesi cijeli broj (0 za prekid): "))

    if number == 0:
        break

    total_sum += number

print(f"Zbroj svih unesenih brojeva je: {total_sum}")
