"""本地 AI 模型推理链路验收测试
验证：torch → transformers → Ollama 本地模型调用
"""
import ollama
import torch
import transformers
import huggingface_hub

def main():
    print("=" * 50)
    print("   本地 AI 推理链路验收")
    print("=" * 50)

    # 1. 库版本
    print(f"\n[torch]          {torch.__version__}")
    print(f"[transformers]   {transformers.__version__}")
    print(f"[huggingface]    {huggingface_hub.__version__}")

    # 2. torch 矩阵运算
    x = torch.randn(3, 4)
    y = torch.randn(4, 5)
    z = torch.mm(x, y)
    print(f"[torch] 矩阵: {x.shape} x {y.shape} = {z.shape} ✓")

    # 3. Ollama 本地模型调用
    models = ["mistral", "hermes3"]
    for model in models:
        resp = ollama.chat(model=model, messages=[
            {"role": "user", "content": "用一句话回复：你是谁？"}
        ])
        reply = resp["message"]["content"][:150]
        print(f"[ollama:{model}] {reply} ✓")

    print("\n" + "=" * 50)
    print("   全部通过 ✓")
    print("=" * 50)

if __name__ == "__main__":
    main()
