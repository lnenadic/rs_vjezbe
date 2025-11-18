import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    else:
        return f"Broj {broj} je neparan."
    
async def main():
    
    lista_brojeva = [random.randint(1, 100) for _ in range(10)] 
    print("Generirani brojevi za provjeru:", lista_brojeva)
    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in lista_brojeva]
    
    rezultati = await asyncio.gather(*zadaci)
    
    for rezultat in rezultati:
        print(rezultat) 

if __name__ == "__main__":
    asyncio.run(main())          