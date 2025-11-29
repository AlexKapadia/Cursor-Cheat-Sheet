# Atomic Agents: Building AI Agents Atomically

**Version:** 2.2.2+

## What It Is

Atomic Agents is a lightweight, modular Python framework for building AI agents and pipelines. It emphasizes modularity, predictability, extensibility, control, and provider agnosticism.

**Key Features:**
- Type-safe agents with generic type parameters
- Schema-driven design using Pydantic
- Streaming support for real-time responses
- Comprehensive hook system for monitoring and error handling
- Multi-provider support (OpenAI, Ollama, Groq, Mistral, Cohere, Anthropic, Gemini, and more)
- Tool ecosystem (Atomic Forge) with pre-built tools
- CLI tool (Atomic Assembler) for managing components

## How to Use It

1. Review the `atomic-agents.mdc` file for detailed architecture and implementation guidelines
2. Install the package: `pip install atomic-agents` or `uv pip install atomic-agents`
3. Follow the examples in the documentation and `atomic-examples/` directory
4. Use the Atomic Assembler CLI to download and manage tools
5. Refer to the code examples and best practices for integration

## Where Information Is From

- **Primary Source**: [GitHub Repository](https://github.com/BrainBlend-AI/atomic-agents)
- **Documentation**: [Official Docs](https://brainblend-ai.github.io/atomic-agents/)
- **PyPI Package**: [atomic-agents on PyPI](https://pypi.org/project/atomic-agents/)
- The content is based on the official repository, documentation, and examples

## How to Build

### Prerequisites

- **Technologies**: Python 3.8+, pip or uv
- **Dependencies**: Instructor, Pydantic, OpenAI (or other LLM provider)

### Setup Steps

1. Install Atomic Agents: `pip install atomic-agents`
2. Set up your LLM provider (OpenAI, Ollama, etc.)
3. Install Instructor: `pip install instructor`
4. Create your first agent following the quickstart examples
5. Optionally install Atomic Forge tools using the CLI: `atomic`

### Local Development

```bash
git clone https://github.com/BrainBlend-AI/atomic-agents.git
cd atomic-agents
uv sync
uv sync --all-packages  # For examples and tools
```

## What to Build With It

### Technologies & Tools

- Python 3.8+
- Instructor (for LLM provider abstraction)
- Pydantic (for schema validation)
- Any LLM provider (OpenAI, Ollama, Groq, Mistral, Cohere, Anthropic, Gemini)

### Recommended Stack

The framework supports building:
- **Chatbots**: Simple to advanced conversational agents
- **RAG Systems**: Retrieval-Augmented Generation applications
- **Research Agents**: Deep research and information extraction
- **Multimodal Agents**: Image and text analysis
- **Orchestration Systems**: Multi-agent coordination
- **Tool-Using Agents**: Agents that interact with external APIs and services

### Example Use Cases

- **Web Search Agents**: Intelligent agents that search and synthesize information
- **YouTube Summarizers**: Extract and summarize video content
- **Data Analysis Agents**: Analyze and extract insights from data
- **Content Generation**: Generate structured content from unstructured input
- **Multi-Agent Systems**: Coordinate multiple specialized agents

---

*For detailed implementation instructions, refer to the `atomic-agents.mdc` file in this directory.*




