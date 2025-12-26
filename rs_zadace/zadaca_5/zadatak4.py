import asyncio

from aiohttp import ClientSession, web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50},
]


async def get_proizvodi(request):
    return web.json_response(proizvodi)


async def get_proizvod(request):
    proizvod_id = int(request.match_info["id"])

    for p in proizvodi:
        if p["id"] == proizvod_id:
            return web.json_response(p)

    return web.json_response(
        {"error": "Proizvod s traženim ID-em ne postoji"}, status=404
    )


def create_app():
    app = web.Application()
    app.router.add_get("/proizvodi", get_proizvodi)
    app.router.add_get("/proizvodi/{id}", get_proizvod)
    return app


async def test_client():
    async with ClientSession() as session:
        print("\nGET /proizvodi")
        async with session.get("http://localhost:8081/proizvodi") as resp:
            print("Status:", resp.status)
            print(await resp.json())

        print("\nGET /proizvodi/id=5")
        async with session.get("http://localhost:8081/proizvodi/5") as resp:
            print("Status:", resp.status)
            print(await resp.json())

        print("\nGET /proizvodi/id=50")
        async with session.get("http://localhost:8081/proizvodi/50") as resp:
            print("Status:", resp.status)
            print(await resp.json())


async def main():
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "localhost", 8081)
    await site.start()

    await asyncio.sleep(0.5)

    await test_client()

    await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
