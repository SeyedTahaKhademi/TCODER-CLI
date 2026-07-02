# TCODER CLI

**Production-Grade AI Coding Agent for Linux**

TCODER is a fully-featured AI software engineering assistant that runs entirely inside Linux terminals. It supports multiple LLM providers, secure API key management, Git integration, and much more!

## معرفی فارسی

TCODER یک دستیار برنامه‌نویسی مبتنی بر هوش مصنوعی برای ترمینال لینوکس است. این ابزار برای کارهای روزمره توسعه مثل گفت‌وگو با مدل‌های زبانی، مدیریت امن کلیدهای API، کار با Git، بررسی کد، تولید مستندات و اجرای ابزارهای کمکی طراحی شده است.

### قابلیت‌ها

- پشتیبانی از چند Provider مثل OpenAI، Anthropic، Gemini، OpenRouter، Groq، DeepSeek، Mistral و مدل‌های محلی مثل Ollama
- نگهداری امن کلیدهای API با keychain سیستم‌عامل و ذخیره‌سازی محلی رمزگذاری‌شده
- رابط تعاملی ترمینال با Textual و خروجی خوانا با Rich
- معماری ماژولار برای توسعه ساده‌تر agentها، providerها و ابزارها
- قابلیت‌های Git برای توضیح diff، کمک به commit و بررسی تغییرات
- سیستم حافظه برای session، پروژه، مکالمه و خلاصه‌سازی خودکار

## Features

- **Provider Agnostic**: Supports OpenAI, Anthropic, Google Gemini, OpenRouter, Groq, DeepSeek, Mistral, and local options like Ollama, vLLM, and LM Studio
- **Secure**: API keys stored using your OS keychain, encrypted local storage, sandbox mode
- **Clean Architecture**: Modular design following Clean Architecture principles
- **Interactive UI**: Rich terminal interface with Textual
- **Git Integration**: AI understands Git, explains diffs, generates commits, resolves conflicts
- **Multi-Agent System**: Planner, Coder, Reviewer, Tester, Documentation, Security, and Git agents
- **Memory System**: Session, project, conversation, and long-term memory with automatic summarization

## Installation

### From PyPI (coming soon)
```bash
pip install tcoder
```

### From source
```bash
git clone https://github.com/SeyedTahaKhademi/TCODER-CLI.git
cd TCODER-CLI
pip install -e .
```

## Quickstart

1. **Login to a provider**
   ```bash
   tcoder login --provider openai --api-key sk-...
   ```

2. **Start chatting!**
   ```bash
   tcoder chat "Explain how to build a Flask REST API"
   ```

3. **Or run interactive mode**
   ```bash
   tcoder
   ```

## Documentation

Project documentation is currently maintained in this repository.

## Releases

GitHub releases are created from version tags.

```bash
git tag v0.1.0
git push origin v0.1.0
```

When a `v*` tag is pushed, GitHub Actions builds the Python package and creates a GitHub Release with the generated `dist` artifacts attached.

## انتشار نسخه جدید

برای ساخت release جدید، نسخه را در `pyproject.toml` و `tcoder/__init__.py` به‌روز کن، سپس یک tag با فرمت `vX.Y.Z` بساز و push کن:

```bash
git tag v0.1.0
git push origin v0.1.0
```

بعد از push شدن tag، workflow ریلیز اجرا می‌شود و فایل‌های build شده را در GitHub Release قرار می‌دهد.

## Contributing

We welcome contributions! Please see our [Contributing Guide](./CONTRIBUTING.md) to get started.

## License

MIT License - see [LICENSE](./LICENSE) for details.
