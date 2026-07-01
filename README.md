# TCODER CLI

**Production-Grade AI Coding Agent for Linux**

TCODER is a fully-featured AI software engineering assistant that runs entirely inside Linux terminals. It supports multiple LLM providers, secure API key management, Git integration, and much more!

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
git clone https://github.com/tcoder-ai/tcoder.git
cd tcoder
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

Full documentation can be found [here](https://tcoder.ai/docs)

## Contributing

We welcome contributions! Please see our [Contributing Guide](./CONTRIBUTING.md) to get started.

## License

MIT License - see [LICENSE](./LICENSE) for details.
