import asyncio


async def f():
    pass


coro = f()
loop = asyncio.get_event_loop()

task = loop.create_task(f())
print(isinstance(task, asyncio.Task))

another_task = asyncio.ensure_future(f())
print(isinstance(another_task, asyncio.Task))

mystery_meat = asyncio.ensure_future(task)
print(mystery_meat is task)

from typing import Any


def listify(x: Any) -> list:
    """ Try hard to convert x into a list """

    """Generally the method is similiar to ensure_future -> return future if it is future else return try to return 
    Task """
    
    if isinstance(x, (str, bytes)):
        return [x]

    try:
        return [_ for _ in x]
    except TypeError:
        return [x]
