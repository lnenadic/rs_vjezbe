import asyncio
import time

import aiohttp


async def posalji_zahtjev(url, port, endpoint, data):

    full_url = f"http://{url}:{port}{endpoint}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(full_url, json=data) as response:
                result = await response.json()
                return {"status": response.status, "data": result}
    except aiohttp.ClientConnectorError:
        print(f"GREŠKA: Ne mogu se povezati na {full_url}")
        print(f"Provjerite je li mikroservis pokrenut na portu {port}")
        return None
    except Exception as e:
        print(f"GREŠKA: {e}")
        return None


async def main():
    url = "localhost"

    brojevi = [10, 20, 30, 40]

    print(f"Testni podaci - Lista brojeva: {brojevi}\n")
    print("-" * 60)

    print("KORAK 1: Konkurentno slanje zahtjeva na mikroservise 1 i 2")
    print("-" * 60)
    start_time = time.time()

    task_zbroj = posalji_zahtjev(url, 8083, "/zbroj", {"brojevi": brojevi})
    task_umnozak = posalji_zahtjev(url, 8084, "/umnozak", {"brojevi": brojevi})

    rezultati = await asyncio.gather(task_zbroj, task_umnozak)

    end_time = time.time()

    zbroj_response = rezultati[0]
    umnozak_response = rezultati[1]

    if not zbroj_response or not umnozak_response:
        print("Greška: Nisu dobiveni odgovori od svih mikroservisa")
        return

    print(f"\n Mikroservis 1 (Zbroj) - Status: {zbroj_response['status']}")
    print(f" Odgovor: {zbroj_response['data']}")

    print(f"\n Mikroservis 2 (Umnožak) - Status: {umnozak_response['status']}")
    print(f" Odgovor: {umnozak_response['data']}")

    print(f"\nVrijeme izvršavanja (konkurentno): {end_time - start_time:.2f} sekundi")

    if zbroj_response["status"] != 200 or umnozak_response["status"] != 200:
        print("\nGreška: Mikroservisi nisu vratili uspješan odgovor")
        return

    zbroj = zbroj_response["data"]["zbroj"]
    umnozak = umnozak_response["data"]["umnozak"]

    print("\n" + "-" * 60)
    print("KORAK 2: Sekvencijalno slanje zahtjeva na mikroservis 3")
    print("-" * 60)

    start_time = time.time()

    kolicnik_response = await posalji_zahtjev(
        url, 8085, "/kolicnik", {"zbroj": zbroj, "umnozak": umnozak}
    )

    end_time = time.time()

    if not kolicnik_response:
        print("Greška: Nije dobiven odgovor od trećeg mikroservisa")
        return

    print(f"\n Mikroservis 3 (Količnik) - Status: {kolicnik_response['status']}")
    print(f" Odgovor: {kolicnik_response['data']}")

    print(f"\nVrijeme izvršavanja (sekvencijalno): {end_time - start_time:.2f} sekundi")

    print("\n" + "-" * 60)
    print("FINALNI REZULTATI")
    print("-" * 60)
    print(f"Ulazni podaci: {brojevi}")
    print(f"Zbroj: {zbroj}")
    print(f"Umnožak: {umnozak}")
    if kolicnik_response["status"] == 200:
        print(f"Količnik (umnožak / zbroj): {kolicnik_response['data']['kolicnik']}")
    print("-" * 60)


if __name__ == "__main__":
    asyncio.run(main())
