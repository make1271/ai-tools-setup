# AI 模型构建工具 — Windows 本地安装记录

> 仓库地址：https://github.com/make1271/ai-tools-setup

本机环境：Windows 11 x64，境内网络（无代理），硬盘 C/D/E 三块。

## 下载地址

| 工具 | 下载 |
|------|------|
| GPT4All | https://www.nubigpt.com/ |
| LM Studio | https://lmstudio.ai/download |
| Jan | https://github.com/janhq/jan/releases/latest |

## 静默安装命令

```powershell
# LM Studio (NSIS)
Start-Process "LM-Studio-x.x.x-x-x64.exe" -ArgumentList "/S" -Wait

# Jan (NSIS)
Start-Process "Jan_x.x.x_x64-setup.exe" -ArgumentList "/S" -Wait
```

## 已安装工具

| 工具 | 版本 | 主程序 | 类型 |
|------|------|--------|------|
| GPT4All | latest | `C:\Users\make\gpt4all\bin\chat.exe` | 桌面 GUI |
| LM Studio | 0.4.14-4 | `E:\LM-Studio-0.4.14-4-x64\LM Studio\LM Studio.exe` | 桌面 GUI |
| Jan | 0.8.0 | `C:\Users\make\AppData\Local\Programs\jan\Jan.exe` | 桌面 GUI |

## 安装踩坑

### LM Studio
- 官网下载页是 Next.js SPA，命令行无法获取直链
- `irm https://lmstudio.ai/install.ps1 | iex` 装的是 llmster 无头版，非 GUI
- GUI 版需手动从 https://lmstudio.ai/download 下载 exe
- 静默安装：`LM-Studio-xxx.exe /S`

### Jan
- GitHub Release 下载极慢（~18KB/s），需耐心
- 官网下的 `Jan AI Installer.exe`(1.3MB) 是 .NET web 下载器，非完整包
- 完整包从 GitHub Releases 下载：`Jan_0.8.0_x64-setup.exe`（约 180MB）
- 静默安装：`Jan_xxx.exe /S`

### GPT4All
- 33MB exe 是 Qt web 下载器，安装时需联网拉完整包

## 本地 Ollama 模型

已拉取 8 个模型（详见下方），共占用约 177GB：

| 模型 | 大小 |
|------|------|
| hermes3:latest | 4.7 GB |
| qwen2.5:72b | 47 GB |
| llama3.3:70b | 42 GB |
| mistral:latest | 4.4 GB |
| glm-5:cloud | 云端 |
| gpt-oss:120b-cloud | 云端 |
| lfm2:latest | 14 GB |
| gpt-oss:120b | 65 GB |

## Python 推理库

虚拟环境：`C:\Users\make\.workbuddy\binaries\python\envs\default`（Python 3.13.12）

### 安装命令

```bash
# 激活虚拟环境
Scripts\activate

# 清华镜像安装（国内快速）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn \
  torch transformers ollama
```

### 已安装

| 库 | 版本 | 说明 |
|----|------|------|
| torch | 2.12.0 (CPU) | 无 NVIDIA GPU，CPU 版 |
| transformers | 5.9.0 | HuggingFace 模型加载 |
| ollama | 0.6.2 | Ollama Python 客户端 |
| huggingface-hub | 1.17.0 | HF 模型下载 |
| safetensors | 0.7.0 | 安全模型格式 |
| numpy | 2.4.6 | 数值计算 |
| llama-cpp-python | — | ❌ Python 3.13 无预编译 wheel，需 Visual C++ Build Tools 源码编译 |
