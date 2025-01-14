import asyncio

async def a():
    print("Hello")
    await asyncio.sleep(3)  # 3초 기다리기

async def b():
    print("World")

async def main():
    await asyncio.gather(a(), b())  # a(), b()를 병렬 수행

asyncio.run(main()) # 3초를 기다리지 않아도 다음 문장이 출력됨, 하지만 프로그램 종료는 3초 후에 됨
