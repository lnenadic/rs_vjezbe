def provjera_lozinke(lozinka):

    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"

    if len(lozinka) <= 8 or len(lozinka) > 15:
        return "Lozinka mora sadržavati između 8 i 15 znakova"

    if not any(char.isupper() for char in lozinka) or not any(char.isdigit() for char in lozinka):
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"

    return "Lozinka je jaka!"


lozinka = input("Unesite lozinku: ")
rezultat = provjera_lozinke(lozinka)
print(rezultat)
