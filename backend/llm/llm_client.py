"""
LLM API 客户端 — 异步调用 DeepSeek
"""
import httpx
from backend.config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL


async def chat(prompt: str, system: str = "你是一个地理知识助手") -> str:
    """调用 DeepSeek API，返回完整回复"""
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{DEEPSEEK_BASE_URL}/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.7,
                "max_tokens": 500,
            },
            timeout=30.0,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
