"""
路由拆分 —— 从零理解
运行：python routing_demo.py
访问：http://127.0.0.1:8001/docs
"""
from fastapi import FastAPI, APIRouter
import uvicorn

# ============================================================
# 第1步：不拆分 —— 所有路由写一起
# ============================================================
# app = FastAPI()
#
# @app.get("/users")
# async def list_users():
#     return [{"name": "张三"}, {"name": "李四"}]
#
# @app.get("/products")
# async def list_products():
#     return [{"name": "电脑"}, {"name": "手机"}]
#
# 问题：users 和 products 混在一起。30 个路由时翻到眼花。

# ============================================================
# 第2步：拆分 —— 把 users 相关的路由搬到另一个变量里
# ============================================================

# 这个 router 专门管 users。它的 prefix 会被自动拼到路径前面。
user_router = APIRouter(prefix="/users", tags=["用户管理"])


@user_router.get("/")
async def list_users():
    return [{"name": "张三"}, {"name": "李四"}]


@user_router.get("/zhangsan")
async def get_user():
    return {"name": "张三", "age": 25}


product_router = APIRouter(prefix="/products", tags=["商品管理"])


@product_router.get("/")
async def list_products():
    return [{"name": "电脑"}, {"name": "手机"}]


# ============================================================
# 第3步：在 app 上把两个 router 挂上去
# ============================================================
app = FastAPI()

app.include_router(user_router)     # "把 user_router 上的所有路由都注册进来"
app.include_router(product_router)  # "把 product_router 上的所有路由都注册进来"

# 结果：app 现在有 3 个路由
# GET /users/
# GET /users/zhangsan
# GET /products/

if __name__ == "__main__":
    print("启动服务器，访问 http://127.0.0.1:8001/docs 看效果")
    uvicorn.run(app, host="127.0.0.1", port=8001)
