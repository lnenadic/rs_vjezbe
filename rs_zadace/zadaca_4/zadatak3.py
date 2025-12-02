import asyncio

import aiohttp


async def get_dog_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://dogapi.dog/api/v2/facts", ssl=False
        ) as response:
            data = await response.json()
            return data["data"][0]["attributes"]["body"]


async def get_cat_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://catfact.ninja/fact", ssl=False) as response:
            data = await response.json()
            return data["fact"]


async def mix_facts(dog_facts, cat_facts):
    mixed_facts = []

    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed_facts.append(dog_fact)
        else:
            mixed_facts.append(cat_fact)

    return mixed_facts


async def main():
    dog_facts = [asyncio.create_task(get_dog_fact()) for _ in range(5)]
    cat_facts = [asyncio.create_task(get_cat_fact()) for _ in range(5)]

    dog_cat_facts = await asyncio.gather(*dog_facts, *cat_facts)

    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

    mixed_facts = await mix_facts(dog_facts, cat_facts)

    print("Mixane činjenice o psima i mačkama:\n")
    for fact in mixed_facts:
        print(fact)


asyncio.run(main())
