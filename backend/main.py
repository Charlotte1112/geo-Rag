from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

