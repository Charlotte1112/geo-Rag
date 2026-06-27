from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.entities import router as entities_router

app = FastAPI(title="山海镜 API")

# CORS：允许前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(entities_router)


@app.get("/api/v1/health")
async def health_check():
    return {"status": "ok"}
