from aiohttp import web


async def kolicnik(request):
    try:
        data = await request.json()
    except:
        return web.json_response({"error": "Nevažeći JSON format"}, status=400)

    if "zbroj" not in data or "umnozak" not in data:
        return web.json_response(
            {"error": "Nedostaju polja 'zbroj' i/ili 'umnozak' u zahtjevu"}, status=400
        )

    zbroj = data["zbroj"]
    umnozak = data["umnozak"]

    if not isinstance(zbroj, (int, float)) or not isinstance(umnozak, (int, float)):
        return web.json_response(
            {"error": "Zbroj i umnožak moraju biti brojevi"}, status=400
        )

    if zbroj == 0:
        return web.json_response(
            {"error": "Dijeljenje s nulom nije moguće - zbroj je 0"}, status=400
        )

    rezultat = umnozak / zbroj
    return web.json_response({"kolicnik": rezultat})


app = web.Application()
app.router.add_post("/kolicnik", kolicnik)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8085)
