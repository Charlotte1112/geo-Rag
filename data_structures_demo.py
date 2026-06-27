"""数据结构性能对比：list vs dict"""
import time
import random
import string

# 生成 1 万条地理实体
def random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

names = [f"山_{random_name()}" for _ in range(10_000)]
# 确保"太白山"在数据里
target_idx = random.randint(0, 9_999)
names[target_idx] = "太白山"

# ===== list 存储 =====
entities_list = [{"name": n, "elevation": random.randint(100, 8000)} for n in names]

# ===== dict 存储 =====
entities_dict = {e["name"]: e for e in entities_list}

# ===== 对比查找"太白山"的耗时 =====

# list 查找：一个个翻
start = time.perf_counter()
for e in entities_list:
    if e["name"] == "太白山":
        found_list = e
        break
list_time = time.perf_counter() - start

# dict 查找：直接取
start = time.perf_counter()
found_dict = entities_dict["太白山"]
dict_time = time.perf_counter() - start

print(f"List 查找耗时: {list_time * 1000:.4f} ms  (O(n) — 线性扫描)")
print(f"Dict 查找耗时: {dict_time * 1000:.4f} ms  (O(1) — 哈希直接定位)")
print(f"Dict 比 List 快 {list_time / dict_time:.0f} 倍")
print(f"\nList 平均要翻 {len(entities_list)//2} 个元素才找到")
print(f"Dict 不管数据量多大，一次定位")
