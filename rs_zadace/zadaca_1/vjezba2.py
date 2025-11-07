user_input = int(input("Unesite neku godinu: "))

if user_input % 4 == 0:
    if user_input % 100 == 0:
        if user_input % 400 == 0:
            print(f"Godina {user_input}. je prijestupna.")
        else:
            print(f"Godina {user_input}. nije prijestupna godina.")
    else:
        print(f"Godina {user_input}. je prijestupna godina.")
else:
    print(f"Godina {user_input}. nije prijestupna godina.")
