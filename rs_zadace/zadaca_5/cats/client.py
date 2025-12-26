import asyncio

from aiohttp import ClientSession


async def main():
    amount = 10

    async with ClientSession() as session:

        async with session.get(f"http://localhost:8086/cat/{amount}") as response:
            facts = await response.json()
            print(f"Dohvaćeno {len(facts)} činjenica")

        async with session.post("http://localhost:8087/facts", json=facts) as response:
            filtered_facts = await response.json()
            print(
                f"Filtrirano {len(filtered_facts)} činjenica koje sadrže 'cat' ili 'cats'"
            )
            print("\nFiltrirane činjenice:")
            for i, fact in enumerate(filtered_facts, 1):
                print(f"{i}. {fact}")


if __name__ == "__main__":
    asyncio.run(main())
