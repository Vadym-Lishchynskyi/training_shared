import asyncio
from datetime import datetime


async def doubler(n):
    for i in range(n):
        yield i, i ** 2
        await asyncio.sleep(1)


async def t1():
    print('hey')
    await asyncio.sleep(1)
    print('there')


async def t2():
    print('hey2')
    await asyncio.sleep(1)
    print('there2')


async def main():
    start = datetime.now()

    result1 = [x async for x in doubler(4)]
    print(result1)
    result2 = {x: y async for x, y in doubler(4)}
    print(result2)
    result3 = {x async for x in doubler(4)}
    print(result3)

    # await t1()
    # await t2()
    #
    # tt1 = asyncio.create_task(t1())
    # tt2 = asyncio.create_task(t2())
    #
    # await tt1
    # await tt2


    res = datetime.now() - start
    print(f'Time: {res}')


async def list_comp():
    a = [x for x in range(6) if x % 2]
    print(a)

asyncio.run(list_comp())
