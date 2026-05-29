# 🐜 蚂二的工作台 — AI 工具与模型全览

> 仓库：https://github.com/make1271/ai-tools-setup  
> 环境：Windows 11 x64 · 境内网络（无代理）· 硬盘 C/D/E

---

## 一、独立智能体

具备独立推理、自主行动能力的 AI。

### 本地大语言模型（Ollama，8 个，177GB）

| # | 模型 | 大小 | 类型 | 能力 |
|---|------|------|------|------|
| 1 | `qwen2.5:72b` | 47 GB | 本地 | 通义千问，中文最强 |
| 2 | `llama3.3:70b` | 42 GB | 本地 | Meta 旗舰，通用推理 |
| 3 | `gpt-oss:120b` | 65 GB | 本地 | 开源 GPT 级，120B 参数 |
| 4 | `lfm2:latest` | 14 GB | 本地 | 轻量快速推理 |
| 5 | `hermes3:latest` | 4.7 GB | 本地 | 指令跟随，工具调用 |
| 6 | `mistral:latest` | 4.4 GB | 本地 | 高效轻量，Mistral AI |
| 7 | `glm-5:cloud` | — | 云端 | 智谱 GLM-5，API 调用 |
| 8 | `gpt-oss:120b-cloud` | — | 云端 | GPT-OSS 云端版 |

### AI 编程助手

| 工具 | 版本 | 类型 |
|------|------|------|
| WorkBuddy（蚂二） | — | 主 AI 助手，当前操控者 |
| OpenAI Codex CLI | 0.130.0 | npm 全局，终端 AI |
| OpenClaw | 2026.5.12 | npm 全局，多模型客户端 |

---

## 二、AI 桌面应用

图形化模型运行与聊天界面。

| # | 应用 | 版本 | 安装路径 |
|---|------|------|----------|
| 1 | **GPT4All** | latest | `C:\Users\make\gpt4all\bin\chat.exe` |
| 2 | **LM Studio** | 0.4.14-4 | `E:\LM-Studio-0.4.14-4-x64\LM Studio\LM Studio.exe` |
| 3 | **Jan** | 0.8.0 | `C:\Users\make\AppData\Local\Programs\jan\Jan.exe` |

---

## 三、Python 推理库

虚拟环境：`C:\Users\make\.workbuddy\binaries\python\envs\default`（Python 3.13.12）

| # | 库 | 版本 | 说明 |
|---|----|------|------|
| 1 | **torch** | 2.12.0 CPU | 深度学习框架，GPU 不可用时 CPU 版 |
| 2 | **transformers** | 5.9.0 | HuggingFace 模型加载与推理 |
| 3 | **ollama** | 0.6.2 | Ollama API Python 客户端 |
| 4 | **huggingface-hub** | 1.17.0 | 模型下载与管理 |
| 5 | **safetensors** | 0.7.0 | 安全高效的模型序列化 |
| 6 | **numpy** | 2.4.6 | 数值计算基础 |
| 7 | llama-cpp-python | — | ❌ 缺 C++ 编译器，待装 |

---

## 安装指南

### 桌面应用

| 应用 | 下载 | 静默安装 |
|------|------|----------|
| GPT4All | https://www.nubigpt.com/ | 手动 |
| LM Studio | https://lmstudio.ai/download | `LM-Studio-xxx.exe /S` |
| Jan | https://github.com/janhq/jan/releases | `Jan_xxx.exe /S` |

### Python 推理库

```bash
# 清华镜像加速
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \
  --trusted-host pypi.tuna.tsinghua.edu.cn \
  torch transformers ollama huggingface-hub safetensors numpy
```

---

## 踩坑记录

- **LM Studio**：官网 Next.js SPA，命令行抓不到直链；`irm ... | iex` 装的是 llmster 无头版
- **Jan**：官网下载器仅 1.3MB，需从 GitHub Releases 拿完整包（~180MB）
- **llama-cpp-python**：Python 3.13 无预编译 wheel，需 Visual C++ Build Tools
- **GitHub**：HTTPS 443 不稳，已配 SSH + 部署密钥；大文件下载用 PowerShell 更稳
