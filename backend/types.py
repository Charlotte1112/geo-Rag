"""核心数据类型定义"""
from typing import Dict, Tuple, Optional, Union, TypedDict


class GeoEntityOutput(TypedDict):
    """精确的返回类型 —— 每个字段有自己的类型"""
    name: str
    lat: float
    lon: float
    elevation: Optional[int]    # 可能拿不到海拔
    province: Optional[str]     # 可能没有省份信息


def process_geo_data(
    name: str,
    coordinates: Tuple[float, float],
    attributes: Dict[str, Optional[Union[int, str]]],
) -> GeoEntityOutput:
    """处理地理数据"""
    lat, lon = coordinates
    elevation = attributes.get("elevation")
    province = attributes.get("province")
    return {
        "name": name,
        "lat": lat,
        "lon": lon,
        "elevation": elevation,
        "province": province,
    }


# 期望调用方式：
result = process_geo_data(
    "太白山",
    (33.96, 107.77),
    {"elevation": 3767, "province": "陕西省"}
)
# VS Code 现在鼠标悬停在 result["elevation"] 上会显示：Optional[int]
# 而 result["name"] 显示：str —— 不再是模糊的 Union
