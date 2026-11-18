import urllib
from concurrent import futures

def solve(number: int) -> bool:
    square_str = str(number ** 2)

    for index in range(len(square_str)):
        left_num = 0 if index == 0 else int(square_str[:index])
        right_num = int(square_str[index:])

        if left_num + right_num == number and right_num != 0:
            return True

    return False

# number = 2
# print(solve(number))

import logging

def try_logging():
    logging.warning("Warning")
    logging.info("Info")

# try_logging()

import asyncio
def try_asyncio():
    def hello():
        print('hello')

    async def bye():
        print('bye')

    async def main():
        await hello()
        bye()

    asyncio.run(main())

# try_asyncio()

def try_futures():
    def thread_func():
        print('thread_func')

    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(thread_func)

# try_futures()

