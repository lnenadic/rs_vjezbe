import asyncio

from aiohttp import ClientSession, web


async def fetch_cat_fact(session):
    async with session.get("https://catfact.ninja/fact") as response:
        data = await response.json()
        return data["fact"]


async def get_cats(request):
    amount = int(request.match_info["amount"])

    async with ClientSession() as session:
        tasks = [fetch_cat_fact(session) for _ in range(amount)]
        facts = await asyncio.gather(*tasks)

    return web.json_response(facts)


app = web.Application()
app.router.add_get("/cat/{amount}", get_cats)

if __name__ == "__main__":
    web.run_app(app, port=8086)
