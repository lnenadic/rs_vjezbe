from aiohttp import web

korisnici = [
    {"ime": "Ivo", "godine": 25},
    {"ime": "Ana", "godine": 17},
    {"ime": "Marko", "godine": 19},
    {"ime": "Maja", "godine": 16},
    {"ime": "Iva", "godine": 22},
]


async def get_punoljetni(request):
    punoljetni = [k for k in korisnici if k["godine"] >= 18]
    return web.json_response(punoljetni)


app = web.Application()
app.router.add_get("/punoljetni", get_punoljetni)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=8082)
