from fastapi import APIRouter

# /explorer로 시작하는 모든 URL을 처리하는 하위 라우터
router = APIRouter(prefix="/explorer")

@router.get("/")
def top():
    return "top explorer endpoint"
