from aiohttp import web


async def check_facts(request):
    data = await request.json()

    filtered_facts = [
        fact for fact in data if "cat" in fact.lower() or "cats" in fact.lower()
    ]

    return web.json_response(filtered_facts)


app = web.Application()
app.router.add_post("/facts", check_facts)

if __name__ == "__main__":
    web.run_app(app, port=8087)
