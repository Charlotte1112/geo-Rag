"""核心探索接口 —— 调用 LLM 分析用户问题"""
import json
from fastapi import APIRouter
from pydantic import BaseModel, Field
from backend.llm.llm_client import chat

router = APIRouter(prefix="/api/v1/explore", tags=["探索"])


class ExploreRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=1000, description="用户问题")


class ExploreResponse(BaseModel):
    entities: list[dict] = []
    answer: str = ""


@router.post("/", response_model=ExploreResponse)
async def explore(request: ExploreRequest):
    """用户提问 → LLM 分析 → 返回结果"""
    analysis = await chat(
        prompt=f"请直接回答以下地理问题，越详细越好。同时提取问题中提到的地理实体。以JSON格式返回：{{\"answer\": \"你的完整回答\", \"entities\": [{{\"name\": \"实体名\", \"type\": \"山/河/湖/省/市\"}}]}}。问题：{request.question}",
        system="你是一个地理知识专家。请基于你的知识直接回答用户的问题，不知道的内容请明确说'不确定'。返回JSON格式，answer字段放完整回答，entities字段放提取的地理实体。",
    )

    try:
        data = json.loads(analysis)
        entities = data.get("entities", [])
        answer = data.get("answer", "")
    except json.JSONDecodeError:
        entities = []
        answer = analysis

    return ExploreResponse(
        entities=entities,
        answer=answer,
    )


@router.post("/direct", response_model=ExploreResponse)
async def explore_direct(request: ExploreRequest):
    """用户提问 → LLM 直接回答（不用 KG，不用 RAG，纯靠 LLM 自身知识）"""
    answer = await chat(
        prompt=request.question,
        system="你是一个地理知识专家。请直接回答用户的问题，尽量详细。你不知道的信息请明确说'不确定'。",
    )

    return ExploreResponse(
        entities=[],
        answer=answer,
    )
