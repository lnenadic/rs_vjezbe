import asyncio
import time

import aiohttp


async def fetch_pozdrav(url, port):
    full_url = f"http://{url}:{port}/pozdrav"
    async with aiohttp.ClientSession() as session:
        async with session.get(full_url) as response:
            return await response.json()


async def main():
    url = "localhost"

    print("--- Sekvencijalno slanje zahtjeva ---")
    start_time = time.time()

    response1 = await fetch_pozdrav(url, 8081)
    print(f"Odgovor sa porta 8081: {response1}")

    response2 = await fetch_pozdrav(url, 8082)
    print(f"Odgovor sa porta 8082: {response2}")

    end_time = time.time()
    print(f"Ukupno vrijeme (sekvencijalno): {end_time - start_time:.2f} sekundi\n")

    print("--- Konkurentno slanje zahtjeva ---")
    start_time = time.time()

    task1 = fetch_pozdrav(url, 8081)
    task2 = fetch_pozdrav(url, 8082)

    results = await asyncio.gather(task1, task2)

    print(f"Odgovor sa porta 8081: {results[0]}")
    print(f"Odgovor sa porta 8082: {results[1]}")

    end_time = time.time()
    print(f"Ukupno vrijeme (konkurentno): {end_time - start_time:.2f} sekundi")


if __name__ == "__main__":
    asyncio.run(main())
