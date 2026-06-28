"""实体搜索相关路由"""
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from backend.llm.llm_client import chat   # ← 导入一次，全文件用

router = APIRouter(prefix="/api/v1/entities", tags=["实体搜索"])

# 模拟数据库（Day 7 替换为真正的 KG 查询）
_entities = [
    {"name": "太白山", "type": "mountain", "elevation": 3767, "province": "陕西省"},
    {"name": "秦岭", "type": "mountain_range", "length_km": 1600, "provinces": ["陕西", "甘肃", "河南"]},
    {"name": "长江", "type": "river", "length_km": 6300, "provinces": ["青海", "四川", "湖北", "上海"]},
]


class SearchRequest(BaseModel):
    """实体搜索请求"""
    q: str = Field(default="", description="搜索关键词")
    entity_type: str = Field(default="", description="实体类型过滤")


class AnalyzeRequest(BaseModel):
    """从文本中提取实体的请求"""
    text: str = Field(..., min_length=10, max_length=5000, description="要分析的文本")


@router.post("/search")
async def search(request: SearchRequest):
    """搜索地理实体（从模拟数据库）"""
    results = []
    for e in _entities:
        if (not request.q or request.q in e["name"]) and (not request.entity_type or e["type"] == request.entity_type):
            results.append(e)
    return {"count": len(results), "results": results}


@router.get("/{name}")
async def get_entity(name: str):
    """按名称获取单个实体"""
    for e in _entities:
        if e["name"] == name:
            return e
    raise HTTPException(status_code=404, detail=f"未找到实体: {name}")


@router.post("/extract")
async def extract_from_text(request: AnalyzeRequest):
    """用 LLM 从文本中提取地理实体 —— 展示跨文件复用 llm_client"""
    prompt = f"""从以下文本中提取所有地理实体（山、河、湖、省、市、山脉、高原等）。
以JSON格式返回：{{"entities": [{{"name": "实体名", "type": "类型"}}]}}

文本：
{request.text}"""

    result = await chat(prompt=prompt, system="只返回JSON，不要其他文字。")

    try:
        data = json.loads(result)
        return {"entities": data.get("entities", [])}
    except json.JSONDecodeError:
        return {"entities": [], "raw": result}
