# Geo-KG 多智能体探索 App — 秋招级深度学习计划 v7

## 🎯 这不是一个项目教程

```
你真正的产出不是这个App，而是：

1. 面试时能自信地说：
   "我独立设计并实现了一个多智能体协作系统，
    从PDF解析到云端部署全栈打通，
    过程中深刻理解了Agent架构、RAG原理、知识图谱工程落地"

2. 遇到任何新问题时，脑子里有：
   "这个问题和我在项目里遇到的XXX本质上是一样的"
   "有A/B/C三种解法，我当时选B是因为..."

3. 代码写出来自带工程味：
   变量命名让人看得懂、异常处理到位、日志可追踪、
   模块边界清晰、能写出为什么这样设计的注释
```

---

## 🧠 我们怎么思考 — 每个模块的标准思维框架

```
对每一个模块，我们不是"怎么做"，而是按这个顺序思考：

Step 1: 问题定义
  "这个模块到底要解决什么问题？不解决会怎样？"
  → 先搞清楚 Why，再讨论 How

Step 2: 方案枚举
  "有哪几种解法？各自的优劣是什么？"
  → 培养"方案思维"——没有银弹，只有取舍

Step 3: 选择论证
  "在这个项目里，我选这个方案，原因是..."
  → 面试官最爱问的："为什么用X而不用Y？"

Step 4: 边界条件
  "什么情况下这个方案会挂？输入为空？并发？超时？"
  → 工程思维——写代码前先想它会怎么坏

Step 5: 实现
  "先写接口定义 → 再写核心逻辑 → 最后处理边界"
  → 结构化编码，不是想到哪写到哪

Step 6: 复盘
  "如果重来一次，我会怎么改？10倍数据量会怎样？"
  → 持续进化的能力
```

---

## 🏗️ 贯穿全程的工程化习惯

```
不是"额外做的事情"，而是融入每个Day的肌肉记忆：

□ Git提交规范
  · 不是 "update code"
  · 而是 "feat: add entity extraction with HanLP+LLM hybrid strategy"
  · 每个小功能一个commit，commit message讲清楚做了什么+为什么

□ 代码审查自查（每次写完代码问自己）
  · 变量名让别人一眼看懂了吗？
  · 异常处理了吗？（不是 try: ... except: pass）
  · 日志打了吗？（关键节点 + 耗时）
  · 如果我3个月后回来看这段代码，能看懂吗？

□ 接口先行
  · 先定义输入输出的数据结构（Pydantic/TypedDict）
  · 再定义函数签名 + docstring
  · 最后才写实现
  · 这样你的代码天然就是"可读的设计文档"

□ 测试习惯
  · 不是"写完再测"，而是"写一段测一段"
  · Happy path + Edge case + Error case 三件套
  · 测试代码也是文档——告诉别人这个函数怎么用

□ 文档习惯
  · README 不是最后写的——每天更新
  · 每个模块有一个 docstring 说明"为什么这样设计"
```

---

## 🎤 面试视角 — 每个模块背后的"面试题"

```
做完不是终点。面试官会从这些角度挑战你：

Day 1-2 (FastAPI):
  "async/await 底层是什么？协程和线程的区别？"
  "FastAPI 为什么快？它的请求生命周期是怎样的？"

Day 3 (Vue 3):
  "Vue 3 的响应式原理？Proxy 比 Object.defineProperty 好在哪里？"
  "虚拟DOM的diff算法大致思路？"

Day 4 (LLM):
  "Token 是什么？为什么不同语言的 token 效率不同？"
  "Temperature=0 和 0.7 的本质区别？什么时候用哪个？"

Day 5 (NLP):
  "NER 的 BIO 标注法是什么？为什么中文 NER 比英文难？"
  "Embedding 为什么能衡量语义相似度？"

Day 6 (RAG):
  "RAG 的完整流程？什么时候 RAG 不够用？"
  "向量检索和关键词检索各自的适用场景？"

Day 7 (KG):
  "知识图谱和关系型数据库的设计思维有什么不同？"
  "图遍历的复杂度？大规模图怎么办？"

Day 8-11 (多Agent):
  "为什么需要多 Agent 而不是单 Agent？"
  "Agent 之间怎么通信？有哪几种模式？各自的优劣？"
  "Orchestrator 应该多'聪明'？规则 vs LLM 决策各有什么优劣？"
  "多 Agent 系统怎么调试？怎么知道是哪个 Agent 出了问题？"

Day 12-13 (部署):
  "Docker 和虚拟机的区别？容器化解决了什么问题？"
  "反向代理的作用？Nginx 怎么做负载均衡？"

Day 14-15 (系统设计):
  "如果用户量增长100倍，你的系统瓶颈在哪？怎么优化？"
  "如果要把这个系统做成 SaaS，需要加什么？"
```

---

## 📐 项目架构总览

```
┌─────────────────────────────────────────────────────────────────┐
│               多智能体协作系统 (LangGraph 编排)                    │
│                                                                 │
│  🎯 Orchestrator → [🌍Geo ‖ 🔗KG ‖ 📄RAG ‖ 🖼️Image]           │
│                  → ✍️Synthesis → 🛡️Critique                    │
│                                                                 │
│  每个 Agent = System Prompt + Tools + LLM                        │
│  GraphState = 共享白板（TypedDict）                              │
│  并行执行 = asyncio.gather                                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  后端: FastAPI + LangChain + LangGraph                           │
│  前端: Vue 3 + Vant UI + 高德地图 + PWA                          │
│  知识: NetworkX KG + ChromaDB + BM25 + bge Embedding             │
│  部署: Docker + Nginx + 云服务器                                  │
├─────────────────────────────────────────────────────────────────┤
│  数据流: PDF → 解析 → NER → KG三元组 + RAG索引                   │
│  查询流: 用户问题 → Orchestrator → 多Agent并行 → 融合 → 回答      │
└─────────────────────────────────────────────────────────────────┘
```

**8个智能体：**

| Agent | 一句话职责 | 工具数 |
|-------|-----------|--------|
| 🎯 Orchestrator | 分析意图→分解任务→调度Agent | 0（调其他Agent） |
| 🌍 GeoAgent | 地名→坐标→地图配置 | 3 |
| 🔗 KGAgent | 实体查询→关系遍历→子图 | 4 |
| 📄 RAGAgent | 向量+关键词混合检索 | 3 |
| 🖼️ ImageAgent | 本地图库+Unsplash | 2 |
| ✍️ SynthesisAgent | 融合结果→生成回答 | 0（纯写作） |
| 🛡️ CritiqueAgent | 核查事实→修正 | 0（纯审查） |

---

## 🗓️ 15天 × 10小时 = 150小时深度学习

---

## Day 1：Python 工程化基础 + 项目骨架

### 核心思维
```
今天的关键转变：从"写脚本"到"写工程"

脚本思维：一个文件、全局变量、print调试、路径硬编码
工程思维：分层结构、类型安全、日志系统、配置分离

面试官看你的代码时会通过这些细节判断你：
  · 有没有在团队里写过代码
  · 有没有被Code Review毒打过
  · 有没有维护过超过一个月的项目
```

### 上午 5h：Python 深度

**第1节 (1h)：类型系统 — 不只是标注，是契约**
```
表面学：
  · type hints 语法：str, int, list[T], dict[K,V], Optional[T], Union[A,B]

深入问：
  · Python的类型标注"不强制"——那为什么还要写？
    → IDE自动补全 + mypy静态检查 + 自文档化 = 团队协作的基础设施
  · 什么时候用 TypeAlias？什么时候用 NewType？
  · Protocol 和 ABC 的区别？（结构化子类型 vs 名义子类型）

动手：
  · 定义我们项目的数据类型（EntityType枚举、GeoCoordinate dataclass）
  · 用 mypy 检查类型错误
  · 体验：一个类型错误在生产环境可能造成的后果
```

**第2节 (1.5h)：数据结构选型 — 选错数据结构比选错算法更致命**
```
表面学：
  · list/tuple/set/dict 的API

深入问：
  · list vs tuple：可变 vs 不可变 → 内存布局 → 适用场景完全不同
  · dict 的哈希表实现 → 为什么 key 必须可哈希？
  · 什么时候用 set 而不是 list？（去重 + O(1)查找 vs O(n)查找）
  · 推导式只是语法糖吗？→ 性能差异（list推导比for循环append快20-40%）

动手：
  · 1万条实体记录 → 用list vs dict vs set 分别做查找 → 对比耗时
  · 体验 O(n) vs O(1) 在真实数据上的差异
```

**第3节 (1.5h)：函数进阶 + 错误处理**
```
表面学：
  · 函数定义、参数、返回值

深入问：
  · *args/**kwargs 本质是解包操作符 → 灵活但丢失了类型信息
  · 装饰器 = 高阶函数 + 闭包 → @app.get("/") 到底做了什么？
  · 异常处理的三层哲学：
    L1：try/except 兜底 — 不让程序挂
    L2：具体异常类型 — 数据库挂了和网络挂了处理方式不同
    L3：异常链 (raise ... from ...) — 保留原始上下文

动手：
  · 写一个 @retry(max_attempts=3, backoff=2) 装饰器
  · 写一个 @log_call 装饰器（打印函数名+参数+耗时）
  · 理解 FastAPI 的 @app.get 也是装饰器
```

**第4节 (1h)：配置管理 + 日志**
```
深入问：
  · 为什么配置要和代码分离？
    → 代码是逻辑，配置是环境。同一份代码在不同环境用不同配置
  · .env 为什么不能提交到 Git？
    → 安全 + 环境隔离。CI有一个.env，生产有另一个.env
  · print() vs logging 的本质区别：
    · print：到stdout，无分级，无时间戳，无来源
    · logging：到任何地方，有DEBUG/INFO/WARNING/ERROR四级，带时间戳和调用栈

动手：
  · Pydantic Settings 加载 config.yaml + .env
  · loguru 配置（彩色输出 + 文件轮转 + 结构化格式）
  · 验证：配置写错时启动就报错，而不是跑到一半才挂
```

### 下午 5h：项目骨架搭建

**第5节 (1.5h)：环境管理 + 项目初始化**
```
深入问：
  · venv vs conda vs poetry vs pipenv → 什么时候用哪个？
  · requirements.txt vs pyproject.toml → 后者是PEP标准
  · pip install 到底做了什么？（下载→解压→复制到site-packages→注册entry_points）
  · 为什么会有依赖冲突？pip的依赖解析器怎么工作？

动手：
  · conda create -n geo_rag python=3.11
  · 创建完整目录结构
  · 写 requirements.txt（精确版本号：langchain==0.3.x）
  · git init + .gitignore（.env, data/, __pycache__, *.pyc, .pytest_cache）
```

**第6节 (1.5h)：项目架构设计 — 不是建目录，是建边界**
```
核心思考（我们一起讨论）：
  Q: 为什么需要 backend/api/、backend/services/、backend/agent/ 这种分层？
  A: 依赖方向：api(最外层) → agent/services(业务层) → 数据层
     外层依赖内层，内层不依赖外层
     这意味着：换框架(Flask→FastAPI)只改api层，业务逻辑不动

  Q: 什么时候该拆新文件？什么时候该拆新目录？
  A: 一个文件超过300行→拆文件。一个目录超过10个文件→拆子目录
     拆分的标准是"高内聚低耦合"——被一起修改的放一起

  Q: __init__.py 除了标记为包，还能做什么？
  A: 控制公开接口（__all__）、延迟导入、包级别初始化

动手：
  · 画出依赖图：哪个模块依赖哪个模块？
  · 验证：import backend.api.chat 不应该触发 import backend.ingestion.pdf_parser
```

**第7节 (1.5h)：Git 工程实践**
```
深入问：
  · commit 为什么需要规范？→ 三个月后你要找一个bug，翻commit历史
  · Conventional Commits 规范：feat/fix/refactor/docs/test/chore
  · 什么时候该 amend？什么时候该 rebase？什么时候绝对不要？
  · .gitignore 的本质：告诉 Git "这些文件不应该被追踪"

动手：
  · 初始化 Git 仓库
  · 第一次 commit：项目骨架 + README
  · 写 .gitignore
  · 创建 .env.example（不含真实Key，只有字段名）
```

**第8节 (0.5h)：今日复盘**
```
写日报（不是形式，是思维训练）：
  1. 今天学了哪些新概念？用自己的话解释一遍
  2. 哪个点最有启发？为什么？
  3. 哪个点还不太明白？明天需要深入
  4. 如果面试官问"Python类型系统有什么用"，我怎么回答？
```

---

## Day 2：HTTP 协议 + FastAPI 后端从零搭建

### 核心思维
```
今天的转变：从"调API的人"变成"设计API的人"

面试官不关心你用了FastAPI还是Flask
他关心的是：
  "你为什么选这个路由结构？"
  "如果请求量增长100倍，你的API设计有什么问题？"
  "你怎么保证API的向后兼容性？"
```

### 上午 5h

**第1节 (1.5h)：HTTP 协议本质**
```
表面学：
  · GET/POST/PUT/DELETE、状态码、Header/Body

深入问：
  · HTTP 是无状态协议 → 但我们需要状态怎么办？（Cookie/Session/Token/JWT）
  · GET请求可以有Body吗？→ 规范不禁止，但几乎所有中间件都会忽略
  · 幂等性：GET/PUT/DELETE是幂等的，POST不是 → 这对API设计意味着什么？
  · RESTful 不是规范是风格 → "真正的REST"和"实用的REST"的区别
  · HTTP/1.1 vs HTTP/2 vs HTTP/3 的核心差异

动手：
  · Chrome DevTools → Network面板 → 访问任意网站
  · 逐行解读一个完整的HTTP请求：Request Line → Headers → Body
  · curl 发 GET/POST 请求，观察响应头
  · 理解 Content-Type: application/json 对后端解析意味着什么
```

**第2节 (2h)：FastAPI 核心**
```
表面学：
  · @app.get、Pydantic BaseModel、uvicorn

深入问：
  · FastAPI 为什么快？→ Starlette(异步) + Pydantic(校验) + 自动OpenAPI
  · ASGI vs WSGI：异步网关 vs 同步网关 → 为什么异步更快？
  · 路由匹配算法：FastAPI 怎么知道 /users/123 匹配 @app.get("/users/{id}")？

动手（每个都亲手写）：
  · GET /api/v1/health → {"status": "ok"}
  · GET /api/v1/entities/{name} → 路径参数
  · GET /api/v1/entities?type=mountain → 查询参数
  · POST /api/v1/explore → 请求体 + Pydantic校验
  · 浏览器打开 /docs → 看Swagger自动文档
  · 在Swagger里直接调试API
```

**第3节 (1.5h)：异步编程 — 不是多线程，是协作式多任务**
```
表面学：
  · async def、await、asyncio.gather

深入问：
  · 并发 vs 并行：并发 = 交替执行（单核），并行 = 同时执行（多核）
  · async/await 是协作式多任务：协程主动交出控制权(yield)
  · 和线程的区别：协程切换 = 函数调用(纳秒级)，线程切换 = 内核调度(微秒级)
  · GIL(全局解释器锁)是什么？→ Python同一时刻只有一个线程执行Python代码
    但IO操作会释放GIL → 所以async对IO密集型有用，对CPU密集型没用
  · 为什么 await 只能出现在 async def 里？
    → await会挂起当前协程 → 只有协程才能被挂起

动手：
  · 写两个版本：同步串行 vs asyncio.gather并发
  · 测耗时：3个1秒的IO操作 → 同步3秒 vs 异步1秒
  · 理解：为什么你的API需要async？（FastAPI的并发处理）
```

### 下午 5h

**第4节 (2h)：API 路由设计**
```
工程思考（一起讨论）：
  Q: 路由应该怎么组织？
  A: 按资源分，不按功能分
     ✓ /api/v1/entities/{name}         按资源
     ✗ /api/v1/get-entity-by-name      按功能（RPC风格）

  Q: 版本号 /v1/ 什么时候加？
  A: 第一天就加。因为你将来一定会改API，版本号是向后兼容的保险

  Q: 搜索用GET还是POST？
  A: 简单搜索用GET(?q=xxx)，复杂搜索用POST(body里放复杂查询条件)
     但是GET有URL长度限制(~2000字符)，POST没有

动手：
  · APIRouter 拆分路由（entities.py / explore.py / graph.py）
  · 在 main.py 中 app.include_router()
  · CORS中间件配置（允许前端跨域）
  · 全局异常处理器：所有未捕获异常统一返回JSON
```

**第5节 (1.5h)：Pydantic 深度**
```
深入问：
  · Pydantic v2 为什么比 v1 快？→ 用Rust重写了核心校验逻辑(pydantic-core)
  · model_dump() vs dict() → v2用model_dump，v1用dict
  · field_validator vs model_validator：单字段校验 vs 跨字段校验
  · 嵌套模型：复杂JSON结构的优雅表示

动手：
  · 定义 ExploreRequest(question, history, need_images)
  · 定义 ExploreResponse(entities, primary_entity, images, knowledge, map_config)
  · 添加 field_validator：question不能为空、不能超过1000字
  · 测试：传错误类型 → Pydantic的错误信息够清晰吗？
```

**第6节 (1h)：API 测试**
```
工程思维：
  · 先写测试，还是先写代码？→ 先写接口定义和测试骨架，再写实现
  · 测试不仅是验证，更是文档——告诉别人这个API怎么用

动手：
  · pytest + httpx.AsyncClient 写API测试
  · 测三种情况：正常返回 / 参数错误 / 服务器内部错误
  · 用 pytest.mark.parametrize 批量测试多种输入
```

**第7节 (0.5h)：今日复盘**
```
写日报 + 准备面试回答：
  "async/await 的本质是什么？为什么Python需要它？"
  "RESTful API 设计有哪些原则？"
```

---

## Day 3：Vue 3 响应式原理 + 前后端联调

### 核心思维
```
今天的转变：从"用框架"到"理解框架做了什么"

面试官不关心你用了Vue还是React
他关心的是：
  "响应式系统是怎么实现的？"
  "虚拟DOM解决了什么问题？又带来了什么问题？"
```

### 上午 5h

**第1节 (1.5h)：Vue 3 响应式系统 — 比API更重要的是原理**
```
表面学：
  · ref、reactive、computed、watch 的用法

深入问：
  · Vue 2用Object.defineProperty，Vue 3用Proxy → 为什么换？
    defineProperty: 只能拦截get/set，不能拦截新增属性、删除属性、数组索引
    Proxy: 拦截13种操作，包括 has/deleteProperty/ownKeys 等
  · ref vs reactive 的本质区别：ref包装基本类型，reactive包装对象
    为什么基本类型需要ref？→ JS的Proxy只能代理对象
  · computed 的缓存机制：依赖不变就不重新计算
    和 method 的区别：method每次调用都重新执行
  · watch vs watchEffect：显式指定依赖 vs 自动追踪

动手：
  · Chrome console 中手动修改 ref.value → 观察DOM自动更新
  · 写一个小的响应式系统：用Proxy自己实现reactive（20行代码）
  · 理解：Vue 3的核心逻辑比你想象的简单
```

**第2节 (1.5h)：虚拟DOM + Diff算法**
```
深入问：
  · 为什么要虚拟DOM？→ 直接操作DOM很贵（重排重绘）
    虚拟DOM = 在JS里做diff（便宜）→ 最小化真实DOM操作（贵）
  · Diff算法的核心思想：
    1. 同层比较（不跨层，O(n) 而不是 O(n³)）
    2. 类型不同→直接替换子树
    3. key属性优化列表diff
  · 为什么v-for必须加key？→ 没有key时Vue用"就地复用"策略，可能导致状态错乱

动手：
  · 写一个带v-for的列表 → 加key vs 不加key → 观察更新行为差异
  · 用Chrome Performance面板看DOM更新耗时
```

**第3节 (2h)：组件化设计**
```
工程思考（一起讨论）：
  Q: 什么时候该拆组件？
  A: 复用 ≥ 3次 → 拆。单个组件 > 200行 → 拆。逻辑和UI可以分离 → 拆。

  Q: Props 向下，Events 向上 → 为什么不能反过来？
  A: 单向数据流 = 可预测。如果子组件可以改父组件的数据，bug的源头无从追踪

  Q: 全局状态 vs 局部状态 → 怎么选？
  A: 只有一个组件用 → 局部。多个组件共享 → props/emits。
     跨页面共享 → provide/inject 或 Pinia

动手：
  · 拆5个组件：SearchBar / MapView / ImageGallery / KnowledgeCard / SourceList
  · 父组件通过props传数据，子组件通过emits发事件
  · 画组件树：哪些组件嵌套哪些？
```

### 下午 5h

**第4节 (1.5h)：Vant UI + 移动端适配**
```
动手：
  · 引入 Vant 4 CDN
  · Search / Card / Tag / Loading / Toast / Tabbar 组件
  · rem 适配（postcss-pxtorem 或手动设置根字体大小）
  · Safe Area 适配（iPhone刘海不遮挡内容）
```

**第5节 (1.5h)：fetch API 封装**
```
工程思考：
  · 为什么需要封装fetch？→ 统一错误处理、自动加Header、环境切换
    dev环境调localhost:8000，prod环境调/api（同域）

动手：
  · 封装 api.explore(query) / api.getEntities(keyword) / api.getGraph(entities)
  · 错误处理三层：
    · 网络断开 → "请检查网络"
    · HTTP 4xx → "请求参数有误"
    · HTTP 5xx → "服务器开小差了，请稍后重试"
  · Loading状态管理（请求前=true，请求后=false，请求失败也要=false）
```

**第6节 (1.5h)：CORS + 前后端联调**
```
深入问：
  · 同源策略为什么存在？→ 防止CSRF攻击（恶意网站冒充你发请求）
  · CORS是"放松"同源策略的安全机制
  · 预检请求(OPTIONS)的触发条件：非简单请求 → POST+JSON头 → 触发预检
  · 前端代理 vs 后端CORS → 开发环境用哪个？生产环境用哪个？

动手：
  · 故意不配CORS → 浏览器报错信息逐行解读
  · 配置CORSMiddleware → 验证
  · DevTools Network面板看OPTIONS预检请求
  · 完整联调：搜索"太白山" → 后端返回JSON → 前端渲染
```

**第7节 (0.5h)：今日复盘**
```
准备面试回答：
  "Vue 3的响应式原理？为什么换Proxy？"
  "虚拟DOM的作用？Diff算法的大致思路？"
  "跨域问题怎么解决？CORS的原理？"
```

---

## Day 4：LLM 编程 — 把大模型当"函数"用

### 核心思维
```
今天的转变：LLM不是魔法，是一个"输入文本→输出文本"的函数

面试官会问：
  "Token是什么？为什么会影响成本和性能？"
  "Temperature=0和0.7的区别？为什么代码生成要用低温度？"
  "怎么让LLM稳定地返回JSON？"
```

### 上午 5h

**第1节 (1.5h)：LLM 本质理解**
```
表面学：
  · 调API、填Prompt、拿结果

深入问：
  · LLM本质 = 自回归语言模型 = 给定前文预测下一个token
    "中国的首都是" → 预测概率最高的下一个词 → "北京"
    每一步都拼接回去再预测下一步 → 这就是"生成"
  · Token ≠ 字。中文约1.5字符/token，英文约4字符/token
    为什么中文token效率更高？→ 中文每个字信息密度更大
  · Context Window = LLM的"工作记忆"
    为什么不是越大越好？→ 注意力复杂度O(n²)，越大越慢越贵
    而且LLM对长文中部的信息关注不够（Lost in the Middle效应）
  · Temperature 控制输出的"熵"
    T→0：几乎每次都选最高概率的token → 确定性高（适合代码、抽取）
    T→1：按概率分布采样 → 多样性高（适合写作、创意）

动手：
  · 在DeepSeek Tokenizer工具里看不同文本的Token数
  · 同一段话，中英文各多少Token？→ 直观感受token效率差异
  · Temperature=0 vs 1 各跑5次对比 → 观察输出确定性差异
```

**第2节 (2h)：Prompt Engineering 系统化**
```
深入问：
  · Prompt不是"写一句话"——是"和LLM的编程语言"
  · 结构化输出的三种方式：
    1. Prompt里写"只返回JSON" → 不稳定，LLM可能加废话
    2. JSON Mode（部分API支持）→ 强制JSON但没Schema校验
    3. Tool Calling / Structured Output → 最可靠，LLM输出被约束到Schema
  · Few-Shot 为什么有效？→ LLM是Pattern Matching Machine
    给示例 = 告诉它你想要的"模式"

动手（同一个任务，对比三种Prompt）：
  · V1(简单)："从文本中提取地理实体"
  · V2(结构化)：定义实体类型+JSON格式+约束条件
  · V3(Few-Shot)：加2个示例 → 对比抽取质量
  · 观察：V3比V1好多少？哪个实体类型最容易漏？
```

**第3节 (1.5h)：LLM Client 封装**
```
工程思考：
  · 为什么需要封装？→ 不只是换个API Key，而是：
    · 统一错误处理（超时、限流、网络错误）
    · 重试策略（指数退避）
    · 日志追踪（每次调用记日志：用了多少token、耗时多少）
    · 成本控制（预算是按token计的）

动手：
  · llm_client.py：封装DeepSeek API调用
  · chat(messages, temperature=0.7) → 完整回复
  · chat_stream(messages) → 流式输出（SSE）
  · 异常处理：APIError / RateLimitError / TimeoutError → 分别处理
```

### 下午 5h

**第4节 (2h)：实现 QueryAnalyzer**
```
工程思考：
  · 为什么要分析查询？→ 不同的查询需要不同的检索策略
    "太白山海拔多少？" → KG查属性就够了
    "秦岭的地质特征？" → 需要RAG检索文档
    "比较秦岭和太行山" → 需要多实体KG + RAG

动手：
  · 实现 QueryAnalyzer.analyze(query) → QueryAnalysis
  · Prompt设计：提取实体 + 判断查询类型 + 推荐检索策略
  · 解析LLM输出为结构化数据（Pydantic.parse_raw）
  · 处理LLM返回非法JSON的情况（```json```包裹、尾部逗号）
```

**第5节 (1.5h)：实现初步 Explore API**
```
动手：
  · POST /api/v1/explore
  · 当前阶段：只做LLM分析（KG和RAG后续接入）
  · 返回：entities + analysis + recommended_strategy
  · 前端展示LLM的分析结果
```

**第6节 (1h)：LLM 最佳实践讨论**
```
讨论（我们一起）：
  · 什么时候用LLM，什么时候不用？
    → LLM擅长：理解语义、推理、生成
    → 不适合：精确计算、确定性规则、高频调用
  · API Key安全：永远不提交到Git → .env + .gitignore
  · 成本估算：一次调用多少钱？（输入token数×单价 + 输出token数×单价）
  · 为什么高并发场景不建议直接调LLM？→ 贵 + 慢 + 有速率限制
```

**第7节 (0.5h)：今日复盘**
```
准备面试回答：
  "Temperature的本质是什么？为什么代码生成建议用低温度？"
  "你怎么样让LLM稳定返回JSON？有哪些方案？"
  "Token是什么？为什么中文比英文token效率高？"
```

---

## Day 5：PDF 解析 + 中文 NLP 基础

### 核心思维
```
今天的转变：PDF不是文本文件，是"电子纸张"

面试官会问：
  "NLP的BIO标注法是什么？为什么中文NLP需要分词？"
  "正则表达式的回溯问题？re.search和re.match的区别？"
```

### 上午 5h

**第1节 (1h)：PDF 格式本质**
```
理解：PDF不是Word。它把每个字符放在精确坐标上，没有"段落"概念。
→ 所以复制出来的文字顺序可能错
→ 所以双栏排版会打乱阅读顺序

动手：用PyMuPDF拆开一个PDF，看block/line/span层级结构
```

**第2节 (1.5h)：PDF 解析器实现**
```
实现 pdf_parser.py：
  · PyMuPDF 提取文本（按block组织，保留坐标信息）
  · 双栏检测（分析所有block的x坐标分布）
  · pdfplumber 提取表格

工程思考：什么时候用PyMuPDF？什么时候用pdfplumber？
  → 纯文本用PyMuPDF（快），表格用pdfplumber（准）
```

**第3节 (1.5h)：文本清洗管线**
```
设计清洗管线（每个步骤一个函数，可组合）：
  1. normalize_unicode() — 全角→半角
  2. remove_headers_footers() — 正则去页眉页脚
  3. fix_line_breaks() — 合并段落内换行
  4. remove_citation_markers() — 去引用标记
  5. normalize_whitespace() — 统一空白

工程思考：为什么用管线模式而不是一个大函数？
  → 可测试（每个步骤单独测）、可复用、可重新组合
```

**第4节 (1h)：正则表达式系统化**
```
深入问：
  · 贪婪匹配 vs 非贪婪匹配 → '.*' vs '.*?'
  · 回溯问题 → 某些正则在长文本上指数级慢
  · re.search vs re.match → match从字符串开头匹配
  · 命名捕获组 → (?P<name>...) → 可读性提升

动手：为每个关系类型写一个正则模板
  "X位于Y" → LOCATED_IN
  "X发源于Y" → ORIGINATES_AT
  "X海拔YYYY米" → 属性elevation
```

### 下午 5h

**第5节 (1.5h)：NLP基础 — 分词、词性、NER**
```
为什么中文比英文难？
  英文：空格天然分词 → "I love Beijing"
  中文：没有空格 → "我爱北京"

分词是中文NLP的基石，分词错了，后面全错：
  "武汉市长江大桥" → "武汉/市长/江大桥" 还是 "武汉市/长江/大桥"？

NER的BIO标注法：
  太白山 → B-MOUNTAIN I-MOUNTAIN I-MOUNTAIN
  位于   → O O
  陕西省 → B-PROVINCE I-PROVINCE I-PROVINCE

动手：用jieba做分词实验 + 添加自定义词典观察变化
```

**第6节 (1.5h)：HanLP NER + LLM 混合策略**
```
为什么混合？
  HanLP：快（CPU 1ms/句）、免费、知识面限于训练数据
  LLM：慢（API 500ms）、花钱、知识面广、能理解上下文

策略：HanLP第一遍 → LLM补充HanLP漏掉的实体
→ 兼顾速度和查全率

动手：实现混合NER，对比纯HanLP vs 纯LLM vs 混合的效果
```

**第7节 (1.5h)：实体消歧 + 共指消解**
```
实体消歧：同一个东西不同名字
  "珠峰" = "珠穆朗玛峰" = "Mount Everest"

共指消解：代词指代什么
  "太白山位于陕西。该山是秦岭最高峰。"→"该山"=太白山

实现：
  1. 精确匹配 → 别名表匹配 → 编辑距离 → Embedding相似度
  2. 规则："该X" → 最近提到的X类型实体
```

**第8节 (0.5h)：今日复盘**
```
准备面试回答：
  "NER的BIO标注法？为什么中文NLP需要分词？"
  "正则的贪婪匹配和回溯问题？"
```

---

## Day 6：RAG — 检索增强生成

### 核心思维
```
今天的转变：从"直接问LLM"到"先检索再问LLM"

为什么需要RAG？
  LLM的知识有截止日期 → RAG给LLM外挂最新知识
  LLM容易"幻觉" → RAG给答案提供事实依据
  LLM没有私有知识 → RAG把私有文档变成可检索的知识
```

### 上午 5h

**第1节 (1h)：Embedding — 文字怎么变成数字**
```
直观理解（不搞数学推导）：
  把文本放到高维空间 → 相似的文本靠得近
  "太白山很高" 和 "秦岭海拔很高" → 靠很近
  "太白山很高" 和 "今天天气不错" → 离很远

余弦相似度：衡量两个向量的"方向"有多接近
  为什么用余弦不用欧氏距离？→ 方向比绝对距离更有意义

动手：3句话向量化 → 算余弦相似度 → PCA降维到2D可视化
```

**第2节 (1h)：分块策略 — RAG的核心难题**
```
分块太大：语义稀释 → 什么都说了≈什么都没说
分块太小：语义不完整 → "太白山，位于" ← 信息不完整
分块正好：取决于你的场景和Embedding模型

三种策略对比：
  固定大小(500字) → 简单但可能切在句子中间
  按段落 → 语义完整但块大小不均
  语义分块 → 按语义边界切，最优但实现复杂

动手：三种分块策略实现 + 对比块质量和大小分布
```

**第3节 (1.5h)：ChromaDB 向量存储**
```
HNSW算法：分层+图 → 牺牲一点点精度换万倍速度

动手：
  · 初始化 ChromaDB PersistentClient
  · 批量写入chunks + embeddings + metadata
  · 实现 search(query, top_k=10)
  · 实现 filter_by_source(pdf_name)
```

**第4节 (1.5h)：BM25 稀疏检索**
```
向量检索擅长语义（"美丽"="漂亮"）
BM25擅长精确匹配（"太白山"≠"太伯山"）
两者结合 = 查全率+查准率都有保障

动手：jieba分词 + rank-bm25索引 → 搜索对比
```

### 下午 5h

**第5节 (1h)：RRF 混合检索融合**
```
为什么不直接加权求和？
→ 向量分数和BM25分数分布不同，不能直接加
RRF：只看排名不看分数 → score = 1/(k+rank)

动手：RRF融合实现 → 对比纯向量/纯BM25/RRF混合的效果
```

**第6节 (1.5h)：RAG 完整管线**
```
离线：PDF → 清洗 → 分块 → Embedding → ChromaDB
在线：提问 → Embedding问题 → 检索+BM25 → RRF → 拼Prompt → LLM生成

动手：scripts/build_rag_index.py 一键构建
```

**第7节 (1.5h)：RAG Prompt 设计**
```
RAG的Prompt模板：
  "基于以下资料回答。如果资料中没有，请明确说明。"
  给每个chunk编号 → LLM回答时引用编号 → 可追溯

动手：对比有RAG vs 无RAG的回答质量（同一问题）
```

**第8节 (0.5h)：今日复盘**
```
准备面试回答：
  "RAG的完整流程？什么时候RAG不够用？"
  "向量检索和关键词检索各自的适用场景？为什么需要混合？"
```

---

## Day 7：知识图谱 — 从文本到结构化知识

### 核心思维
```
今天的转变：知识不只有"文本片段"，还有"实体和关系"

图思维 vs 表思维：
  表思维："给我所有属于XX山脉的山峰" → JOIN两张表
  图思维："从秦岭出发，沿着belongs_to反向走，找到所有山峰" → 图遍历
  图擅长关系推理，表擅长精确查询
```

### 上午 5h

**第1节 (1h)：知识图谱是什么**
```
Google搜索"秦岭" → 右侧的信息卡片 → 那就是知识图谱
三元组 = (实体, 关系, 实体) = (秦岭, 位于, 中国)

和数据库的区别：
  DB擅长："海拔>3000的山有哪些？"
  KG擅长："发源于秦岭的河流有哪些？它们的支流又有哪些？"
  → 图的优势在多跳关系推理
```

**第2节 (1h)：Schema 设计 — 数据的宪法**
```
Schema的粒度取舍：
  太细 → 每个小山都建节点 → 爆炸
  太粗 → 所有都叫"地理实体" → 没用

设计原则：用户会问什么？→ 决定建什么实体和关系
  用户会问"属于哪个山脉？" → 需要 BELONGS_TO
  用户会问"发源于哪里？" → 需要 ORIGINATES_AT
  用户不会问"岩石类型" → 先不加（MVP不要过度设计）
```

**第3节 (1.5h)：规则模板抽取**
```
为什么规则优先？→ 确定性高、速度快、零成本、可解释
规则覆盖60-70% → 剩下的用LLM补

动手：实现8-10个正则模板
  "X位于Y（省/市）"  → LOCATED_IN
  "X发源于Y（山脉）"  → ORIGINATES_AT
  ...
```

**第4节 (1.5h)：LLM Few-Shot 补充抽取**
```
规则覆盖不了的：隐性关系、复杂句式
LLM Few-Shot补充 → 合并 → 去重 → 置信度加权
```

### 下午 5h

**第5节 (1h)：NetworkX 建图**
```
为什么NetworkX不是Neo4j？
  NetworkX：import就能用，零运维。几百个节点完全够用。
  Neo4j：需要单独服务，运维成本高。适合百万级节点。

但Schema设计保持兼容：将来换Neo4j只需改存储层，接口不变
→ 这就是分层架构的价值
```

**第6节 (1h)：图查询接口**
```
实现：点查 / 邻居遍历 / 路径搜索 / 子图提取 / 统计

面试常问：图遍历复杂度？
  BFS：O(V+E)，适合找最短路径
  DFS：O(V+E)，适合找所有路径（可能很多！）
  所以我们的get_neighbors限制了depth（防止全图遍历）
```

**第7节 (1.5h)：KG + RAG 结果融合**
```
KG擅长：精确的关系 → "太白山属于秦岭"
RAG擅长：描述性知识 → "秦岭的地质特征包括..."

两者互补 → 融合后给LLM → 既有结构化事实又有叙事背景
```

**第8节 (0.5h)：今日复盘**
```
准备面试回答：
  "知识图谱和关系数据库的设计思维有什么不同？"
  "什么时候用图数据库，什么时候用关系数据库？"
```

---

## Day 8-11：多智能体系统（已在前面详细展开）

Day 8：单Agent→多Agent过渡 + LangGraph初体验
Day 9：构建5个专业Agent（Geo/KG/RAG/Image/Synthesis）
Day 10：Orchestrator + LangGraph完整编排 + 并行执行
Day 11：CritiqueAgent + 流式多Agent + 冲突解决 + 调优

---

## Day 12：系统集成 + 全链路联调

### 核心思维
```
今天的转变：从"各模块都能跑"到"整个系统稳定可靠"

工程思维：
  代码能跑 ≠ 系统可靠
  可靠 = 正常情况正确 + 异常情况不崩溃 + 出问题能追踪
```

### 全天安排

**第1节 (1.5h)：全链路日志追踪**
```
给每个请求生成request_id → 经过的每个模块都带上
出问题时 → 一个request_id查所有日志 → 定位问题

动手：
  · 中间件生成request_id
  · loguru.bind(request_id=...) 全局传递
  · 追踪一个完整请求 → 分析每个环节耗时
```

**第2节 (2h)：错误场景覆盖**
```
测试12种失败场景：
  空输入 / 超长输入 / 无网络 / 500错误 / LLM超时 /
  高德API超限 / Unsplash超限 / KG无结果 / RAG无结果 /
  LLM返回非法JSON / 并发请求 / 大文件上传

每个场景：前端友好提示 + 后端日志记录 + 不影响其他功能
```

**第3节 (1.5h)：性能基线**
```
记录基线：
  API p50/p95/p99 响应时间
  Agent平均迭代次数
  各Tool调用频率和耗时
  向量检索 vs BM25 耗时对比
  LLM API调用占比（通常是最大头）

优化方向：并行调用、缓存、减少Agent迭代
```

**第4节 (2h)：搜索体验 + 答案质量**
```
搜索优化：输入建议 / 搜索历史 / 热门搜索 / 空状态设计
答案优化：KG三元组格式化 / RAG结果去重 / 多实体比较
来源引用：PDF名+页码+可点击链接
```

**第5节 (1.5h)：评估脚本**
```
20道测试题（实体查询/关系查询/多跳/比较）
每道题定义"关键信息点"
跑一遍 → 统计覆盖率 → 迭代
```

---

## Day 13：Docker + 云部署

### 核心思维
```
今天的转变：从"我电脑上能跑"到"任何电脑上都能跑"

Docker的本质理解：
  不是虚拟机！Docker共享宿主机内核
  虚拟机：虚拟整个OS，几GB，慢启动
  容器：进程隔离，几MB，秒启动

类比：Docker像集装箱
  没有集装箱：每个码头用不同的方式装卸 → 乱
  有集装箱：所有码头都能装卸标准集装箱 → 简单
```

### 全天安排

**第1节 (1h)：Docker 基础**
```
docker run hello-world → 理解pull+run
docker ps / images / logs / exec
```

**第2节 (1.5h)：Dockerfile 编写**
```
FROM python:3.11-slim
COPY requirements.txt → pip install
COPY 代码 → 配置
CMD uvicorn

为什么先COPY requirements再COPY代码？
→ 利用Docker层缓存：requirements没变就不重新pip install
```

**第3节 (1h)：docker-compose**
```
多容器编排：app（FastAPI）+ nginx（反向代理+静态文件）
volumes：持久化KG + 向量库数据
```

**第4节 (1h)：Nginx 配置**
```
反向代理：客户端→Nginx→FastAPI
好处：统一入口、静态文件不经过Python、HTTPS终结
```

**第5节 (2h)：云部署**
```
选云服务器 → SSH登录 → 安装Docker
git clone → docker-compose up -d
域名解析(A记录) → Certbot HTTPS证书
```

**第6节 (1h)：部署检查清单**
```
HTTPS证书 / API可访问 / PWA安装 / 数据持久化 / 日志 / 监控
```

---

## Day 14：系统回顾 — 全局视角

### 核心思维
```
今天的转变：从"实现者"到"设计者"

一个好的工程师和一个优秀的工程师的区别：
  好的工程师：能实现功能
  优秀的工程师：能解释为什么这样实现，知道如果不这样会出什么问题
```

### 全天安排

**第1节 (2h)：完整数据流追踪**
```
用户输入"太白山属于哪个山脉？"
  → 前端fetch → Nginx反向代理 → FastAPI路由
  → Orchestrator分析 → [KGAgent‖GeoAgent]并行
  → Synthesis融合 → Critique核查 → 返回JSON
  → 前端渲染地图+图片+知识卡片

追踪每个环节：谁在等谁？哪里可以更快？
```

**第2节 (1.5h)：设计模式回顾**
```
分层架构：api→services→data（所有项目通用）
策略模式：坐标解析（KG→高德→LLM）
适配器模式：LLM Client（DeepSeek→可换GPT）
管道模式：文本清洗（可组合的步骤）
观察者模式：Agent的intermediate_steps回调
```

**第3节 (1.5h)：技术决策复盘**
```
为什么FastAPI不是Flask？为什么LangGraph不是AutoGen？
为什么ChromaDB不是Pinecone？为什么NetworkX不是Neo4j？
每次选择都是trade-off：简单vs强大、快vs稳、单人vs团队
```

**第4节 (1h)：Agent 模式迁移**
```
GeoAgent的多Agent模式可用于：
  客服系统 / 数据分析 / 代码助手 / 旅游规划

核心公式不变：Agent = LLM + Tools + 循环
```

---

## Day 15：进阶方向 + 秋招准备

### 核心思维
```
知道上限在哪 + 知道下一步学什么 = 系统性的成长路径
```

### 全天安排

**第1节 (1.5h)：项目深化方向**
```
6个方向：KG升级Neo4j / RAG加Reranker / 多Agent协作 /
  3D地形可视化 / 知识自动更新 / 微服务拆分

不是要做，是知道"如果要做该怎么做"
→ 面试时能聊技术选型
```

**第2节 (1.5h)：面试模拟 — 项目介绍**
```
我会模拟面试官问你：
  "请介绍一下这个项目"
  "你最大的技术挑战是什么？"
  "如果重新做，你会怎么改进？"
  "这个系统的瓶颈在哪？怎么优化？"

你的回答应该：
  有结构（背景→目标→方案→结果）
  有深度（不只说做了什么，说为什么这样做）
  有反思（承认局限，知道改进方向）
```

**第3节 (1h)：秋招学习路线**
```
三阶段：
  初级（你已完成✅）→ 中级（Advanced RAG, Fine-tuning, TypeScript）
  → 高级（Agent框架内部, RLAIF, 分布式系统）
```

**第4节 (1h)：项目收尾**
```
README完善 / 代码注释补充 / Git commit整理 / 演示录制
```

---

## 附录A：每天执行模板

```
每节课我们的协作节奏：

[5min]   我：今天学什么 + 为什么重要
[15-20min] 我：核心概念讲解（对话式，我问你答）
[5min]   你：提问题，确认理解
[5min]   我：给你接口定义 + 思考框架
[30-60min] 你：动手写代码（卡住随时问我）
[10-15min] 我：审阅你的代码 + 指出改进点
[5-10min] 你：根据反馈修改
[5-10min] 讨论："如果换一种方式会怎样？" "面试官问这个你怎么答？"
```

---

## 附录B：简历项目描述（完成后的输出）

```
项目名称：Geo-KG 多智能体地理知识探索系统

技术栈：
  后端：Python, FastAPI, LangChain, LangGraph
  前端：Vue 3, Vant UI, 高德地图 JS API, PWA
  AI：DeepSeek, RAG(ChromaDB+BGE), 知识图谱(NetworkX)
  部署：Docker, Nginx, 云服务器

项目描述：
  设计并实现了一个多智能体协作的地理知识探索系统。
  系统包含8个专业Agent（Orchestrator/Geo/KG/RAG/
  Image/Synthesis/Critique），通过LangGraph编排实现
  任务分解、并行执行和结果融合。
  支持从PDF文献中自动构建知识图谱和RAG索引，
  用户可通过移动端PWA进行自然语言探索，
  系统自动定位地图、展示景观图片和知识解读。

项目亮点：
  · 多智能体架构：Orchestrator调度+专业Agent并行执行，节省>50%时间
  · 知识图谱+混合检索：自研规则+LLM双引擎三元组抽取
  · 移动端PWA：Vue3+Vant+高德地图，支持离线使用和桌面安装
  · 全栈交付：从PDF解析到Docker云部署的完整工程链路
```

---

> **信念**：15天后，你不仅有一个项目，更有"我能独立设计和交付AI应用"的底气。
> 秋招面试时，你能自信地讲出每一个技术决策的"为什么"。