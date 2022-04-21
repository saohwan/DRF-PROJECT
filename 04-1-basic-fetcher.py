import time
import requests


def fetcher(session, url):  # fetcher 라는 함수는 인자로 session을 받고 url 을 받는다.
    with session.get(url) as response:
        return response.text


def main():
    url = "https://naver.com"

    # session = requests.Session
    # session.get(url)
    # session.close() 7,8,9 라인의 코드를 아래 with 를 사용하여 세션을 열고 닫는 기능을 모두 수행.

    with requests.Session() as session:
        urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 10초
