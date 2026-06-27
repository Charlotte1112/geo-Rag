"""
装饰器：从零开始理解
"""
import time
import functools


# ============================================================
# 第1步：一个普通函数，什么都不加
# ============================================================
def geocode(place_name: str) -> dict:
    time.sleep(0.2)
    return {"place": place_name, "lat": 33.96, "lon": 107.77}


print("=== 第1步：原始函数 ===")
print(geocode("太白山"))
print()


# ============================================================
# 第2步：装饰器公式
#
#   def 装饰器名(func):
#       def wrapper(*args, **kwargs):
#           # --> 这里写额外逻辑
#           result = func(*args, **kwargs)
#           # --> 这里也可以写额外逻辑
#           return result
#       return wrapper
#
# ============================================================

# ----- 计时装饰器 -----
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} 耗时 {time.perf_counter() - start:.3f}s")
        return result
    return wrapper


# ----- 重试装饰器 -----
def retry(max_attempts: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"[retry] 第{attempt}次失败，重试中...")
                    time.sleep(0.5)
            return None
        return wrapper
    return decorator


# ============================================================
# 第3步：使用装饰器
# ============================================================

@timer
def fast_geocode(place_name: str) -> dict:
    time.sleep(0.1)
    return {"place": place_name, "lat": 33.96, "lon": 107.77}


@retry(max_attempts=3)
def unstable_geocode(place_name: str) -> dict:
    import random
    if random.random() < 0.5:
        raise ConnectionError("网络超时")
    return {"place": place_name, "lat": 33.96, "lon": 107.77}


print("=== 第3步：@timer 效果 ===")
fast_geocode("太白山")
print()

print("=== 第3步：@retry 效果 ===")
try:
    result = unstable_geocode("太白山")
    print(f"调用成功: {result}")
except ConnectionError:
    print("3次重试全部失败")
