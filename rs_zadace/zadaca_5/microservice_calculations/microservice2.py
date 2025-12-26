import operator
from functools import reduce

from aiohttp import web


async def umnozak(request):
    try:
        data = await request.json()
    except:
        return web.json_response({"error": "Nevažeći JSON format"}, status=400)

    if "brojevi" not in data:
        return web.json_response(
            {"error": "Nedostaje polje 'brojevi' u zahtjevu"}, status=400
        )

    brojevi = data["brojevi"]

    if not isinstance(brojevi, list):
        return web.json_response(
            {"error": "Polje 'brojevi' mora biti lista"}, status=400
        )

    if len(brojevi) == 0:
        return web.json_response(
            {"error": "Lista brojeva ne smije biti prazna"}, status=400
        )

    try:
        rezultat = reduce(operator.mul, brojevi, 1)
        return web.json_response({"umnozak": rezultat})
    except TypeError:
        return web.json_response(
            {"error": "Svi elementi liste moraju biti brojevi"}, status=400
        )


app = web.Application()
app.router.add_post("/umnozak", umnozak)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8084)
