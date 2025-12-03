# LangChain Integration Packages - Comprehensive Guide

## What It Is

This MDC file contains a comprehensive guide to all LangChain Python integration packages. It documents 1000+ integrations across:

- **Chat Models:** Language models from OpenAI, Anthropic, Google, AWS, and many more
- **Embedding Models:** Text embedding models for semantic search
- **Vector Stores:** Databases optimized for vector similarity search
- **Document Loaders:** Components for loading data from various sources
- **Tools & Toolkits:** External tools and services for agent capabilities
- **Key-Value Stores:** Storage systems for caching and state management

The guide is extracted from the official LangChain documentation and includes installation instructions, usage examples, code snippets, feature comparisons, and best practices for each integration category.

## How It Works

This MDC was created by extracting comprehensive information from the LangChain official documentation about integration packages. It follows the scientific-paper-to-mdc-rules format, adapted for technical documentation rather than a scientific paper.

The document includes:
- Complete provider listings with package names
- Installation and setup instructions
- Code examples for each integration type
- Feature comparison tables
- Best practices and optimization tips
- Common pitfalls and warnings
- Implementation patterns and architectures

## How to Use When Building

### Method 1: Reference in Cursor Chat
When building AI agents or LangChain applications, reference this file in your chat:

```
@langchain-integration-packages.mdc I need to set up a RAG pipeline with OpenAI embeddings and Chroma vector store. Show me the code.
```

### Method 2: Open in Cursor
Open the MDC file directly in Cursor to browse all available integrations and find the right one for your use case.

### Method 3: Add to Cursor Rules
Add this file to your Cursor Rules to have the integration information always available when building LangChain applications.

### Method 4: Use Specific Sections
Reference specific sections when you need:
- **Chat Models:** See "Chat Models Integration" section
- **Embeddings:** See "Embedding Models Integration" section
- **Vector Stores:** See "Vector Stores Integration" section
- **Document Loaders:** See "Document Loaders Integration" section
- **Tools:** See "Tools and Toolkits Integration" section

## Key Concepts

### Integration Packages
Separate Python packages for each provider (e.g., `langchain-openai`, `langchain-anthropic`). Each package contains provider-specific implementations that conform to LangChain's standardized interfaces.

### Base Interfaces
All integrations implement standardized base classes:
- `BaseChatModel` for chat models
- `BaseEmbeddings` for embedding models
- `VectorStore` for vector databases
- `BaseLoader` for document loaders
- `BaseStore` for key-value stores

### Standardized APIs
LangChain provides consistent APIs across all providers, abstracting away provider-specific details while maintaining access to provider-specific features when needed.

## Quick Start

1. **Choose Your Components:**
   - Select a chat model provider (e.g., OpenAI, Anthropic)
   - Select an embedding model (e.g., OpenAI, HuggingFace)
   - Select a vector store (e.g., Chroma, Pinecone, Qdrant)

2. **Install Packages:**
   ```bash
   pip install langchain-openai langchain-chroma
   ```

3. **Set Environment Variables:**
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

4. **Use the MDC:**
   Reference the relevant sections in this MDC for code examples and implementation details.

## Contents

The MDC includes:

1. **Overview:** Introduction to LangChain integrations
2. **Popular Providers:** Table of most-used integrations
3. **All Providers:** Complete listing of all supported providers
4. **Chat Models Integration:** Detailed guide for chat model integrations
5. **Embedding Models Integration:** Guide for embedding model integrations
6. **Vector Stores Integration:** Comprehensive vector store guide with feature comparison
7. **Document Loaders Integration:** Document loader guide organized by category
8. **Key-Value Stores Integration:** Guide for caching and state management
9. **Tools and Toolkits Integration:** Guide for extending agent capabilities
10. **Implementation Patterns:** Architecture and design patterns
11. **Code Examples:** Complete working examples for common use cases
12. **Best Practices:** Optimization tips and common pitfalls
13. **Limitations:** Known limitations and constraints
14. **Appendices:** Installation commands, environment variables, error codes

## Related Resources

- **LangChain Comprehensive Guide:** `../langchain/langchain-comprehensive-guide.mdc` - Core LangChain concepts
- **LangGraph Comprehensive Guide:** `../langgraph/langgraph-comprehensive-guide.mdc` - Agent orchestration
- **Official LangChain Docs:** https://docs.langchain.com
- **LangChain Python API:** https://python.langchain.com

## Notes

- This MDC is based on LangChain documentation as of 2025
- Package versions and features may change - always check official documentation for latest information
- Some integrations require specific package versions for certain features
- API keys and credentials should never be committed to version control
- Always test integrations locally before deploying to production
