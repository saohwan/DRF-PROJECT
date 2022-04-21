import asyncio
import time
import aiohttp

import os
import threading


async def fetcher(session, url):  # fetcher 라는 함수는 인자로 session을 받고 url 을 받는다.
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    async with session.get(url) as response:
        return response.text


async def main():
    urls = ["https://google.com", "https://apple.com"] * 50

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end = time.time()
    print(end - start)  # 26초
