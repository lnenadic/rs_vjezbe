import asyncio

# asinkrona funkcija koja simulira odbrojavanje
# svaki put kada dođe do 'await asyncio.sleep(1)',
# korutina prelazi u stanje "suspended"
# kontrolu predaje event loopu, koji nakon tog može pokrenuti druge zadatke
async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        # event loop zakazuje "timer" korutinu da se ponovno pokrene tek nakon 1 sekunde
        # do tada se ne izvršava - u međuvremenu se izvršavaju druge korutine
        await asyncio.sleep(1)
    # po završetku petlje, korutina prelazi u stanje "finished"
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    # create_task registrira korutinu u event loopu kao Task objekt
    # task prelazi u stanje "scheduled" i bit će pokrenut čim event loop dobije priliku
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    # asyncio.gather čeka da svi zadaci završe
    # main korutina se pauzira dok svi timeri ne prijeđu u "finished"
    # u međuvremenu event loop izvršava njihove dijelove jedan po jedan
    await asyncio.gather(*timers)


# asyncio.run kreira event loop, pokreće main korutinu, upravlja svim izvršavanjima
# i zatvara loop kada su sve korutine gotove
asyncio.run(main())