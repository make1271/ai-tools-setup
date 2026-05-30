# AI 模型构建工具 · Windows-PC 全览

> 生成方式：Codex CLI v0.135.0 + Ollama (mistral)  
> 生成时间：2026-05-29  
> 本机环境：Windows 11 x64 · 42GB RAM · 无GPU · 无代理

---

## 一、桌面 AI 应用

| 工具 | 版本 | 安装路径 | 状态 |
|------|------|----------|------|
| LM Studio | 0.4.14-4 | `E:\LM-Studio-0.4.14-4-x64\LM Studio\LM Studio.exe` | ✅ 可用 |
| Jan | 0.8.0 | `C:\Users\make\AppData\Local\Programs\jan\Jan.exe` | ✅ 可用 |
| GPT4All | latest | `C:\Users\make\gpt4all\bin\chat.exe` | ✅ 可用 |

---

## 二、Python 推理库

虚拟环境：`C:\Users\make\.workbuddy\binaries\python\envs\default`（Python 3.13.12）

| 库 | 版本 | 状态 | 备注 |
|----|------|------|------|
| torch | 2.12.0 | ✅ | CPU 版，无 NVIDIA GPU |
| transformers | 5.9.0 | ✅ | HuggingFace 模型加载 |
| ollama | 0.6.2 | ✅ | Ollama Python 客户端 |
| huggingface-hub | 1.17.0 | ✅ | 模型下载与管理 |
| safetensors | 0.7.0 | ✅ | 安全模型序列化 |
| numpy | 2.4.6 | ✅ | 数值计算 |
| llama-cpp-python | — | ❌ | 缺 C++ 编译器，Python 3.13 无预编译 wheel |

---

## 三、Ollama 本地模型

| 模型 | 大小 | 状态 | 说明 |
|------|------|------|------|
| mistral:latest | 4.4 GB | ✅ 可用 | 轻量通用，快启 |
| hermes3:latest | 4.7 GB | ✅ 可用 | 指令跟随，工具调用 |
| qwen2.5:72b | 47 GB | ❌ 内存不足 | 需 48.6GB，剩 46GB |
| llama3.3:70b | 42 GB | ❌ 内存不足 | 需 70GB |
| gpt-oss:120b | 65 GB | ❌ 内存不足 | 需 120GB+ |

---

## 四、云端模型

| 模型 | 状态 | 说明 |
|------|------|------|
| glm-5:cloud | ⚠️ 需 API | 智谱 GLM-5 云端 |
| gpt-oss:120b-cloud | ⚠️ 需 API | GPT-OSS 云端版 |

---

## 五、Codex CLI 状态

| 项目 | 值 |
|------|-----|
| 版本 | v0.135.0 |
| 后端 | Ollama (ollama-launch) |
| 默认模型 | 配置为 gpt-oss:120b，实际可用 mistral/hermes3 |
| 配置文件 | `C:\Users\make\.codex\config.toml` |

---

## 六、已知问题

1. **大模型 OOM**：qwen2.5:72b / llama3.3:70b / gpt-oss:120b 均因内存不足无法加载
2. **llama-cpp-python**：Python 3.13 无预编译 wheel，需 Visual C++ Build Tools
3. **GitHub HTTPS**：端口 443 不稳定，已配 SSH + 部署密钥
4. **LM Studio**：官网 Next.js SPA，命令行无法获取直链
