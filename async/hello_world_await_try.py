import asyncio
import time


async def sleeping(n: int) -> None:
    time.sleep(n)
#   we can not run this function as coro because
#   time.sleep() is not awaitable object


async def main_hello():
    print('Hello main...')
    await asyncio.sleep(5)
    print('...main World!')
    return 'main_hello'


async def sub_main_hello():
    print('Hello sub_main...')
    await asyncio.sleep(2)
    print('... sub_main World!')
    return 'sub_main_hello'


async def main():
    group = await asyncio.gather(main_hello(), sub_main_hello())
    print(group)


asyncio.run(main())
