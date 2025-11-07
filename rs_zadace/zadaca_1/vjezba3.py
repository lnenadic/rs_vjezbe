import random

secret_number = random.randint(1, 100)
broj_je_pogoden = False
attempts = 0

while not broj_je_pogoden:
    guess_input = input("Pogodi broj u rasponu od 1 do 100: ")

    if not guess_input.isdigit():
        print("Unosi se samo cijeli broj. (1-100)")
        continue

    guess = int(guess_input)
    attempts += 1

    if guess < secret_number:
        print("Broj je veći.")
    elif guess > secret_number:
        print("Broj je manji.")
    else:
        broj_je_pogoden = True
        print(f"Bravo, pogodio si u {attempts} pokušaja.")
