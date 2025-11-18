import asyncio

baza_korisnika = [
  {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
  {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
  {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
  {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
  {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
  {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
  {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
  {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik_baza, lozinka):
    await asyncio.sleep(2)
    for unos in baza_lozinka:
        if unos['korisnicko_ime'] == korisnik_baza['korisnicko_ime']:
            if lozinka == unos['lozinka']:
                return f"Korisnik {korisnik_baza['korisnicko_ime']}: Autorizacija uspješna."
            else:
                return f"Korisnik {korisnik_baza['korisnicko_ime']}: Autorizacija neuspješna."
    return f"Korisnik {korisnik_baza['korisnicko_ime']} nije pronađen u bazi lozinki."

async def autentifikacija(korisnik):
    await asyncio.sleep(3)
    for unos in baza_korisnika:
        if unos['korisnicko_ime'] == korisnik['korisnicko_ime'] and unos['email'] == korisnik['email']:
            rezultat = await autorizacija(unos, korisnik.get('lozinka'))
            return rezultat
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."

async def main():
    korisnici = [
      {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'lozinka123'
      },
      {
        'korisnicko_ime': 'lovre123',
        'email': 'lovre123@gmail.com',
        'lozinka': 'lozinka123'
      }
    ]
    
    tasks = [autentifikacija(k) for k in korisnici]

    rezultati = await asyncio.gather(*tasks)

    for r in rezultati:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())