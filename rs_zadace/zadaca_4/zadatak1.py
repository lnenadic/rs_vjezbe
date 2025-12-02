import asyncio
import time

import aiohttp


async def fetch_users():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://jsonplaceholder.typicode.com/users", ssl=False
        ) as resposne:
            return await resposne.json()


async def main():
    start_time = time.time()

    results = await asyncio.gather(*[fetch_users() for i in range(5)])

    users = results[0]
    names = [user["name"] for user in users]
    emails = [user["email"] for user in users]
    usernames = [user["username"] for user in users]

    print("Name:")
    print(names)
    print("\nEmail:")
    print(emails)
    print("\nUsername:")
    print(usernames)

    end_time = time.time()
    print(f"Time to fetch the data: {end_time - start_time:.2f}")


asyncio.run(main())
