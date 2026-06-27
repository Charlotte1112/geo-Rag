"""核心探索接口"""
from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/explore", tags=["探索"])


class ExploreRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000, description="用户问题")


class ExploreResponse(BaseModel):
    entities: list[dict] = []
    answer: str = ""


@router.post("/", response_model=ExploreResponse)
async def explore(request: ExploreRequest):
    """用户提问 → LLM 分析 → 返回结果"""
    # 先返回一个占位，后面接入真正的 LLM 分析
    return ExploreResponse(
        entities=[],
        answer=f"收到你的问题：{request.question}。分析功能接入中..."
    )
