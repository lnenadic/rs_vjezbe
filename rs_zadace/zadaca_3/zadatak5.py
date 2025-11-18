import asyncio

podaci = [
    {'prezime': 'Anić', 'broj_kartice': '4242424242424242', 'CVV': '123'},
    {'prezime': 'Perić', 'broj_kartice': '5105105105105100', 'CVV': '321'},
    {'prezime': 'Jurić', 'broj_kartice': '6011000990139425', 'CVV': '231'}
]

async def secure_data(osoba):
    await asyncio.sleep(3) 
    novi_rijecnik = {
        'prezime': osoba['prezime'],
        'broj_kartice': hash(osoba['broj_kartice']),
        'CVV': hash(osoba['CVV'])
    }
    return novi_rijecnik
    
async def main():
    zadaci = [secure_data(osoba) for osoba in podaci]
    rezultati = await asyncio.gather(*zadaci)
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())      