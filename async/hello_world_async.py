import asyncio
import time


async def main():
    """
    Using function asyncio.run()
    with and without description
    """

    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


# asyncio.run(main())

"""
    Explanation on how asyncio.run() works on the backstage
"""
loop = asyncio.get_event_loop()
# We need loop to run any coroutines -> then we have to create a new task we add it to the loop
# In a single thread we can current loop calling "asyncio.get_running_loop()"
task = loop.create_task(main())
# Our 'main()' is a coroutine function. It won't be executed until we add it to the loop
# Returned object can be used to monitor status of the coroutine(coro)
# and can be canceled 'coro.cancel()'
loop.run_until_complete(task)
# Internally 'asyncio.run' runs 'run_until_complete()'
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()


# The loop can be stopped and closed
# Stopped loop can be restarted but closed loop has gone
# After each 'asyncio.run()' loop is initiated and closed
