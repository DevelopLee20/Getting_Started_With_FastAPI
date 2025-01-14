def test(): # 제너레이터 생성
    yield "Hello"   # 매 호출마다 yield 뒤의 내용 반환
    yield "World"   # 매 호출마다 yield 뒤의 내용 반환

for i in test():
    print(i)
