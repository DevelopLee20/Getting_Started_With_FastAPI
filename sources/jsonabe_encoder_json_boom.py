import datetime
import pytest
from fastapi.encoders import jsonable_encoder   # 파이썬 객체를 JSON으로 인코딩
import json

@pytest.fixture # 테스트 함수들이 공통적으로 사용할 데이터 설정 및 초기화, 다른 테스트 함수에 자동으로 전달됨
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)

def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    json_out = json.dumps(out)
    assert json_out
