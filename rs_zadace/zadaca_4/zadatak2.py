import asyncio

import aiohttp


async def get_cat_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://catfact.ninja/fact", ssl=False) as response:
            data = await response.json()
            return data["fact"]


async def filter_cat_facts(cat_facts):
    return [fact for fact in cat_facts if "cat" in fact.lower()]


async def main():
    tasks = [get_cat_fact() for _ in range(20)]

    cat_facts = await asyncio.gather(*tasks)

    filtered_facts = await filter_cat_facts(cat_facts)

    for fact in filtered_facts:
        print("- ", fact)


asyncio.run(main())
