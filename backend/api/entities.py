"""实体搜索相关路由"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/entities", tags=["实体搜索"])

# 模拟数据库
_entities = [
    {"name": "太白山", "type": "mountain", "elevation": 3767, "province": "陕西省"},
    {"name": "秦岭", "type": "mountain_range", "length_km": 1600, "provinces": ["陕西", "甘肃", "河南"]},
    {"name": "长江", "type": "river", "length_km": 6300, "provinces": ["青海", "四川", "湖北", "上海"]},
]


@router.get("/")
async def search(q: str = "", entity_type: str = ""):
    """搜索地理实体"""
    results = []
    for e in _entities:
        if (not q or q in e["name"]) and (not entity_type or e["type"] == entity_type):
            results.append(e)
    return {"count": len(results), "results": results}


@router.get("/{name}")
async def get_entity(name: str):
    """按名称获取单个实体"""
    for e in _entities:
        if e["name"] == name:
            return e
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail=f"未找到实体: {name}")
