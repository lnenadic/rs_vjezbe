import asyncio

async def fetch_data_web():
    print("Dohvaćanje podataka s weba...")
    await asyncio.sleep(3)  
    print("Podaci dohvaćeni.")
    podaci = [i for i in range(1, 11)]
    return podaci

if __name__ == "__main__":
    rezultat = asyncio.run(fetch_data_web())
    print("Rezultat:", rezultat)