# 山海镜 — 多智能体地理知识探索系统

> 基于知识图谱与RAG增强的多智能体地理信息检索系统
> 从 PDF 文献到云端部署的全栈 AI 应用 —— 秋招级工程实践

## 项目简介

用户输入地理问题（如"太白山属于哪个山脉？"），系统通过 **8 个 AI Agent 协作**，自动完成：地名识别 → 地图定位 → 知识图谱查询 → 文档检索 → 景观图片展示 → 生成答案。

## 技术栈

| 层 | 技术 |
|----|------|
| 多智能体框架 | **LangGraph** — 8 Agent 协作编排，支持并行执行 |
| 后端 | **FastAPI** + LangChain + DeepSeek LLM |
| 前端 | **Vue 3** + Vant UI + 高德地图 JS API + **PWA** |
| 知识图谱 | **NetworkX** — 规则 + LLM 双引擎三元组抽取 |
| RAG 检索 | **ChromaDB** + BGE Embedding + BM25 混合检索 |
| 部署 | **Docker** + Nginx + 云服务器 |

## 核心亮点

- **多智能体协作**：Orchestrator 调度 → Geo/KG/RAG/Image 四个专业 Agent 并行执行 → Synthesis 融合 → Critique 审查，节省 50%+ 响应时间
- **知识图谱 + RAG 双路检索**：结构化关系查询 + 非结构化文档检索互补
- **移动端 PWA**：支持离线使用和桌面安装，体验接近原生 App
- **全栈工程闭环**：从 PDF 解析 → NLP 实体抽取 → KG 构建 → LLM 生成 → 云部署

## 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/你的用户名/geo_Rag.git
cd geo_Rag

# 2. 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env，填入你的 API Key

# 5. 构建知识库
python scripts/build_all.py

# 6. 启动服务
python scripts/run_dev.py
# 浏览器打开 http://localhost:8000
```

## 项目结构

```
geo_Rag/
├── backend/
│   ├── api/          # FastAPI 路由层
│   ├── services/     # 业务逻辑（KG、RAG、Geo、Image）
│   ├── agent/        # 多智能体模块（LangGraph 编排）
│   └── config.py     # 配置管理
├── frontend/         # Vue 3 PWA 前端
├── data/             # PDF 源文件、知识库、向量库
├── scripts/          # 构建与启动脚本
└── tests/            # 测试
```

## 开发周期

15 天 × 10h/天，单人全栈开发。详见 `Geo-KG多智能体探索App-15天秋招级学习计划.md`。

## 开发进度

| Day | 内容 | 产出 | 状态 |
|-----|------|------|:--:|
| 1 | Python 工程化 + 项目骨架 | `types.py` `config.py` 装饰器 demo 数据结构 demo | ✅ |
| 2 | HTTP 协议 + FastAPI 后端 | — | ⏳ |
| 3-15 | 进行中 | — | ⬜
