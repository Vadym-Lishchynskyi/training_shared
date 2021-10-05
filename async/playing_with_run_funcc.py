import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


# Running coroutines one by one
# async def main():
#     print(f'Begin: {time.strftime("%X")}')
#
#     await say_after(1, 'Hello')
#     await say_after(2, 'World')
#
#     print(f'End: {time.strftime("%X")}')
#
# asyncio.run(main())


async def main():
    t1 = asyncio.create_task(say_after(1, 'Hello'))
    t2 = asyncio.create_task(say_after(4, 'World'))

    print(f'Begin: {time.strftime("%X")}')

    await t1
    await t2

    print(f'End: {time.strftime("%X")}')

asyncio.run(main())
