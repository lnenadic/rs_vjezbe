user_input1 = float(input("Unesite prvi broj: "))
user_input2 = float(input("Unesite drugi broj: "))
operator = input("Unesite operator (+, -, *, /): ")
dozoljeni_operatori = ['+', '-', '*', '/']

if operator not in dozoljeni_operatori:
    print("Nepodržani operator!")

if operator == '+':
    rezultat = user_input1 + user_input2
    print("Rezultat operacije", user_input1,
          "+", user_input2, "je", rezultat)
elif operator == '-':
    rezultat = user_input1 - user_input2
    print("Rezultat operacije", user_input1,
          "-", user_input2, "je", rezultat)
elif operator == '*':
    rezultat = user_input1 * user_input2
    print("Rezultat operacije", user_input1,
          "*", user_input2, "je", rezultat)
elif operator == '/':
    if user_input2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")
    else:
        rezultat = user_input1 / user_input2
        print("Rezultat operacije", user_input1,
              "/", user_input2, "je", rezultat)
