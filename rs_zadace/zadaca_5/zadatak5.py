import asyncio

from aiohttp import ClientSession, web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50},
]

narudzbe = []


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


async def post_narudzbe(request):
    data = await request.json()
    proizvod_id = data.get("proizvod_id")
    kolicina = data.get("kolicina")

    if not any(p["id"] == proizvod_id for p in proizvodi):
        return web.json_response(
            {"error": "Proizvod s traženim ID-em ne postoji"}, status=404
        )

    narudzbe.append({"proizvod_id": proizvod_id, "kolicina": kolicina})
    return web.json_response(narudzbe, status=201)


def create_app():
    app = web.Application()
    app.router.add_get("/proizvodi", get_proizvodi)
    app.router.add_get("/proizvodi/{id}", get_proizvod)
    app.router.add_post("/narudzbe", post_narudzbe)
    return app


async def test_client():
    async with ClientSession() as session:
        async with session.get("http://localhost:8081/proizvodi") as r:
            print(r.status, await r.json())

        async with session.get("http://localhost:8081/proizvodi/4") as r:
            print(r.status, await r.json())

        async with session.get("http://localhost:8081/proizvodi/44") as r:
            print(r.status, await r.json())

        async with session.post(
            "http://localhost:8081/narudzbe",
            json={"proizvod_id": 2, "kolicina": 2},
        ) as r:
            print(r.status, await r.json())

        async with session.post(
            "http://localhost:8081/narudzbe",
            json={"proizvod_id": 22, "kolicina": 1},
        ) as r:
            print(r.status, await r.json())


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
