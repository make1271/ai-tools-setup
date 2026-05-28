# AI 模型构建工具 — Windows 本地安装记录

本机环境：Windows 11 x64，境内网络（无代理），硬盘 C/D/E 三块。

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
