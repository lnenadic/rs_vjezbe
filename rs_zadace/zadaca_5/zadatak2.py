from aiohttp import web

proizvodi = [
    {"naziv": "MacbookPro 14'", "cijena": 1200.0, "količina": 10},
    {"naziv": "MacbookPro 16'", "cijena": 1600.0, "količina": 5},
    {"naziv": "Mac Mini", "cijena": 800.0, "količina": 20},
]


# GET /proizvodi
async def get_proizvodi(request):
    return web.json_response(proizvodi)


# POST /proizvodi
async def post_proizvodi(request):
    novi_proizvod = await request.json()
    print("Primljeni proizvodi:", novi_proizvod)

    proizvodi.append(novi_proizvod)

    return web.json_response(proizvodi)


app = web.Application()
app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_post("/proizvodi", post_proizvodi)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=8081)
