import asyncio

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}


async def autentifikacija(korisnicko_ime, lozinka):
    await asyncio.sleep(2)

    if korisnicko_ime not in korisnici or korisnici[korisnicko_ime] != lozinka:
        raise ValueError(f"Neispravni podaci za {korisnicko_ime}")

    return True


async def main():
    zahtjevi = [
        autentifikacija("korisnik1", "lozinka1"),
        autentifikacija("korisnik2", "lozinka"),
        autentifikacija("korisnik3", "lozinka3"),
        autentifikacija("unkown", "na"),
        autentifikacija("korisnik1", "lozinka1"),
    ]

    rezultati = await asyncio.gather(*zahtjevi, return_exceptions=True)
    print(rezultati)

    try:
        await asyncio.wait_for(autentifikacija("korisnik1", "lozinka1"), timeout=1)
    except asyncio.TimeoutError:
        print("Timeout greška")


asyncio.run(main())
