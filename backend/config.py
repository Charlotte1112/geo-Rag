"""
应用配置 —— 从 .env 和环境变量加载，绝不硬编码敏感信息
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from loguru import logger

# 加载 .env 文件
load_dotenv(Path(__file__).parent.parent / ".env")

# ===== LLM 配置 =====
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

# ===== 高德地图配置 =====
AMAP_WEB_KEY = os.getenv("AMAP_WEB_KEY")      # 后端地理编码用
AMAP_JS_KEY = os.getenv("AMAP_JS_KEY")        # 前端地图用

# ===== Unsplash 配置 =====
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

# ===== 数据路径 =====
DATA_DIR = Path(__file__).parent.parent / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
KG_DIR = DATA_DIR / "kg"
VECTOR_STORE_DIR = DATA_DIR / "chroma_db"
IMAGE_DIR = DATA_DIR / "images"

# ===== 日志配置 =====
logger.add(
    DATA_DIR / "logs" / "app.log",
    rotation="10 MB",      # 超过 10MB 自动切文件
    retention="7 days",    # 保留最近 7 天
    level="INFO",
    format="{time} | {level} | {name}:{function}:{line} | {message}",
)

# ===== 启动验证 =====
def validate_config():
    """启动时检查必要配置，缺了就报错，而不是跑到一半挂"""
    missing = []
    if not DEEPSEEK_API_KEY:
        missing.append("DEEPSEEK_API_KEY")
    if not AMAP_WEB_KEY:
        missing.append("AMAP_WEB_KEY")
    if missing:
        raise ValueError(
            f"缺少必要配置: {', '.join(missing)}。"
            f"请复制 .env.example 为 .env 并填入真实值。"
        )
    logger.info("配置加载成功")
