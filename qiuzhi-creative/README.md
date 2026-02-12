# Qiuzhi Creative / 秋芝创意

🇬🇧 **English** | [🇨🇳 中文](#chinese)

## 🇬🇧 Description
**Qiuzhi Creative** is your digital muse and research assistant. It automates the intake of information, allowing you to focus on high-level decision making and creation.

### Capabilities
- **Smart Capture**: Automatically downloads YouTube subtitles (via `yt-dlp`) and article content.
- **Knowledge Processing**: Uses LLM to summarize content into structured Markdown notes (Summary, Insights, Actions).
- **Inbox Management**: Saves everything to a `knowledge/inbox` folder for review.

### Usage
Run the summarizer script manually or via OpenClaw trigger:
```bash
python3 scripts/summarize.py "https://youtube.com/..."
```

---

## <a id="chinese"></a>🇨🇳 描述
**秋芝创意** 是您的数字缪斯和研究助手。它自动化了信息的摄入过程，让您可以专注于高层的决策和创作。

### 核心能力
- **智能捕获**: 自动下载 YouTube 字幕（通过 `yt-dlp`）和文章内容。
- **知识处理**: 利用 LLM 将内容总结为结构化的 Markdown 笔记（包含摘要、洞察、行动项）。
- **收件箱管理**: 将所有生成的内容保存到 `knowledge/inbox` 文件夹等待回顾。

### 使用方法
手动运行摘要脚本，或通过 OpenClaw 触发：
```bash
python3 scripts/summarize.py "https://youtube.com/..."
```
