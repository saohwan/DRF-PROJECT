# pip install aiohttp~=3.7.3

import aiohttp
import asyncio
import time


async def fetcher(session, url):  # fetcher 라는 함수는 인자로 session을 받고 url 을 받는다.
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end = time.time()
    print(end - start)  # 4.27초
