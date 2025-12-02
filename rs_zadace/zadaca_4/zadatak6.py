import asyncio
import random


async def fetch_weather_data(station_id):
    delay = random.uniform(1, 5)
    await asyncio.sleep(delay)

    temperature = random.uniform(20, 25)
    print(
        f"Stanica {station_id} vratila temperaturu: {temperature:.2f}°C (kašnjenje: {delay:.2f}s)"
    )
    return temperature


async def main():
    tasks = []

    for i in range(10):
        task = asyncio.create_task(fetch_weather_data(i))
        tasks.append(task)

    results = []

    for i, task in enumerate(tasks):
        try:
            temperature = await asyncio.wait_for(task, timeout=2)
            results.append(temperature)
        except asyncio.TimeoutError:
            print(f"Stanica {i} nije odgovorila na vrijeme (Timeout).")
            results.append(None)

    valid_temperatures = [t for t in results if t is not None]

    if valid_temperatures:
        avg_temp = sum(valid_temperatures) / len(valid_temperatures)
        print(f"\nProsječna temperatura: {avg_temp:.2f}°C")
    else:
        print("\nNije bilo moguće izračunati prosječnu temperaturu (nema podataka).")


asyncio.run(main())
