from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from backend.api.entities import router as entities_router
from backend.api.explore import router as explore_router

app = FastAPI(title="山海镜 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entities_router)
app.include_router(explore_router)


@app.get("/api/v1/health")
async def health_check():
    return {"status": "ok"}


# 前端静态文件 —— 必须在 API 路由之后注册
frontend_dir = Path(__file__).parent.parent / "frontend"
if frontend_dir.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")

