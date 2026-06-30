"""
Agent 本质演示 —— 用你已有的 llm_client，模拟一次 Agent 循环
运行：.venv/Scripts/python agent_demo.py
"""
import json
import asyncio
from backend.llm.llm_client import chat


# ===== 第1步：定义一个工具（就是一个普通 Python 函数）=====
def search_knowledge_graph(entity_name: str) -> dict:
    """查询知识图谱，返回实体的关系三元组"""
    # 模拟 KG 数据（Day 7 之后会换成真正的 NetworkX 查询）
    kg_data = {
        "太白山": {
            "triples": [
                {"subject": "太白山", "predicate": "BELONGS_TO", "object": "秦岭"},
                {"subject": "太白山", "predicate": "LOCATED_IN", "object": "陕西省"},
                {"subject": "太白山", "predicate": "HAS_ELEVATION", "object": "3767m"},
            ]
        },
        "秦岭": {
            "triples": [
                {"subject": "秦岭", "predicate": "SPANS", "object": "陕西,甘肃,河南"},
                {"subject": "汉江", "predicate": "ORIGINATES_AT", "object": "秦岭"},
                {"subject": "嘉陵江", "predicate": "ORIGINATES_AT", "object": "秦岭"},
            ]
        }
    }
    result = kg_data.get(entity_name, {"triples": []})
    return {entity_name: result}


# ===== 第2步：告诉 LLM 它有哪些工具可用 =====
TOOL_DESCRIPTION = """
你有一个工具：search_knowledge_graph(entity_name)
- 功能：输入一个地名（如"太白山"），返回该实体在知识图谱中的所有关系三元组
- 实体名必须精确匹配（如"太白山"不能写成"太白"）
"""


# ===== 第3步：Agent 循环 —— 思考 → 行动 → 观察 → 再思考 → 最终回答 =====
async def agent_demo(user_question: str):
    print(f"👤 用户：{user_question}\n")

    # ---- Round 1：LLM 思考并决定是否调工具 ----
    print("🧠 LLM 第1次思考...")

    # 拼一个 Prompt，让 LLM 选择：是直接回答，还是调用工具
    decision_prompt = f"""
{TOOL_DESCRIPTION}

用户问题：{user_question}

请决定你的下一步。如果你需要调用工具，输出JSON：
{{"action": "call_tool", "tool": "search_knowledge_graph", "input": "实体名"}}

如果你不需要工具，直接输出：
{{"action": "answer", "answer": "你的回答"}}

只输出JSON，不要其他文字。
"""
    decision = await chat(decision_prompt, system="你是地理知识助手。")
    decision = json.loads(decision.strip())
    print(f"   LLM 决定：{decision['action']}\n")

    # ---- Round 2：如果 LLM 要调工具，就执行工具，把结果喂回去 ----
    if decision["action"] == "call_tool":
        tool_name = decision["tool"]
        tool_input = decision["input"]

        print(f"🔧 执行工具：{tool_name}(\"{tool_input}\")")
        tool_result = search_knowledge_graph(tool_input)
        print(f"   工具返回：{json.dumps(tool_result, ensure_ascii=False)}\n")

        # ---- 把工具结果喂给 LLM，让它生成最终回答 ----
        print("🧠 LLM 第2次思考（基于工具结果）...")

        final_prompt = f"""
{TOOL_DESCRIPTION}

用户问题：{user_question}

你调用了工具 search_knowledge_graph("{tool_input}")，得到了以下结果：
{json.dumps(tool_result, ensure_ascii=False)}

请基于这些数据回答用户的问题。如果数据中没有答案，明确说"数据不足"。
"""
        final_answer = await chat(final_prompt, system="你是地理知识助手，只基于提供的工具结果回答。")
        print(f"\n📝 最终回答：{final_answer}")

    else:
        # LLM 觉得不需要工具，直接回答
        print(f"📝 直接回答：{decision['answer']}")


if __name__ == "__main__":
    asyncio.run(agent_demo("太白山属于哪个山脉？海拔多少？"))
