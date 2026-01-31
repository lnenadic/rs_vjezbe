import hashlib

from aiohttp import web

korisnici = [
    {
        "korisnicko_ime": "admin",
        "lozinka_hash": "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b",
    },
    {
        "korisnicko_ime": "markoMaric",
        "lozinka_hash": "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa",
    },
    {
        "korisnicko_ime": "ivanHorvat",
        "lozinka_hash": "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302",
    },
    {
        "korisnicko_ime": "Nada000",
        "lozinka_hash": "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d",
    },
]


def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


async def register(request):
    try:
        data = await request.json()
        korisnicko_ime = data.get("korisnicko_ime")
        lozinka = data.get("lozinka")

        if not korisnicko_ime or not lozinka:
            return web.json_response(
                {"error": "Nedostaju korisničko ime ili lozinka!"}, status=400
            )

        if any(k["korisnicko_ime"] == korisnicko_ime for k in korisnici):
            return web.json_response(
                {"error": "Korisničko ime već postoji!"}, status=409
            )

        lozinka_hash = hash_data(lozinka)
        novi_korisnik = {"korisnicko_ime": korisnicko_ime, "lozinka_hash": lozinka_hash}
        korisnici.append(novi_korisnik)

        return web.json_response(
            {
                "message": "Korisnik uspješno registriran!",
                "korisnicko_ime": korisnicko_ime,
            },
            status=201,
        )

    except Exception as e:
        return web.json_response(
            {"error": f"Greška pri registraciji: {str(e)}"}, status=500
        )


async def login(request):
    try:
        data = await request.json()
        korisnicko_ime = data.get("korisnicko_ime")
        lozinka = data.get("lozinka")

        if not korisnicko_ime or not lozinka:
            return web.json_response(
                {"error": "Nedostaju korisničko ime ili lozinka!"}, status=400
            )

        korisnik = next(
            (k for k in korisnici if k["korisnicko_ime"] == korisnicko_ime), None
        )

        if not korisnik:
            return web.json_response({"error": "Korisnik ne postoji!"}, status=404)

        lozinka_hash = hash_data(lozinka)

        if lozinka_hash != korisnik["lozinka_hash"]:
            return web.json_response({"error": "Neispravna lozinka!"}, status=401)

        return web.json_response(
            {"message": "Uspješna prijava", "korisnicko_ime": korisnicko_ime},
            status=200,
        )

    except Exception as e:
        return web.json_response({"error": f"Greška pri prijavi: {str(e)}"}, status=500)


def create_app():
    app = web.Application()

    app.router.add_post("/register", register)
    app.router.add_post("/login", login)

    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host="0.0.0.0", port=9000)
