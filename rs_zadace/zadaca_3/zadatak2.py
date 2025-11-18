import asyncio
import time

async def fetch_data_users():   
    print("Dohvaćanje podataka o korisnicima...")
    await asyncio.sleep(3)  
    print("Podaci o korisnicima dohvaćeni.")
    korisnici = [
        {"id": 1, "ime": "Lovre", "prezime": "Lovrić"},
        {"id": 2, "ime": "Luka", "prezime": "Lukić"},
        {"id": 3, "ime": "Lucija", "prezime": "Lučić"},
    ]
    return korisnici

async def fetch_data_items():   
    print("Dohvaćanje podataka o podacima...")
    await asyncio.sleep(5)  
    print("Podaci o podacima dohvaćeni.")
    proizvodi = [
        {"id": 1, "naziv": "Proizvod X", "cijena": 100},
        {"id": 2, "naziv": "Proizvod Y", "cijena": 200},
        {"id": 3, "naziv": "Proizvod Z", "cijena": 300},
    ]
    return proizvodi

#ispisi rezultate dohvaćanja podataka
async def main():
    start_time = time.time()
    
    dohvacanje_korisnika = fetch_data_users()
    dohvacanje_proizvoda = fetch_data_items()
    
    korisnici, proizvodi = await asyncio.gather(dohvacanje_korisnika, dohvacanje_proizvoda)
    print("--- Korisnici ---")
    for korisnik in korisnici:
        print(korisnik)

    print("--- Proizvodi ---")
    for proizvod in proizvodi:
        print(proizvod)
    
    end_time = time.time()
    print(f"Dohvaćanje podataka završeno je u {end_time - start_time:.2f} sekundi.")
    
if __name__ == "__main__":
    asyncio.run(main())