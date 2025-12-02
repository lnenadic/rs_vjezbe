import asyncio

import aiohttp


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url, ssl=False, timeout=aiohttp.ClientTimeout(total=5)
        ) as response:
            text = await response.text()
            return text


async def main():
    urls = ["https://example.com", "https://httpbin.org/get", "https://api.github.com"]

    tasks = []
    for url in urls:
        task = fetch_url(url)
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    for i in range(len(urls)):
        content = results[i]
        print(f"Fetched {len(content)} characters from {urls[i]}")


asyncio.run(main())
