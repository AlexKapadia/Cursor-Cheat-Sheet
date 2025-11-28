# Gemini AI Integration Guide

A professional reference guide for implementing and working with Google's Gemini AI API.

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Authentication and API Keys](#authentication-and-api-keys)
4. [Available Models](#available-models)
5. [API Endpoints](#api-endpoints)
6. [Integration Patterns](#integration-patterns)
7. [Request and Response Formats](#request-and-response-formats)
8. [Best Practices](#best-practices)
9. [Common Use Cases](#common-use-cases)
10. [Error Handling](#error-handling)
11. [Rate Limits and Quotas](#rate-limits-and-quotas)
12. [Security Considerations](#security-considerations)
13. [Code Examples](#code-examples)
14. [Troubleshooting](#troubleshooting)
15. [Resources and Documentation](#resources-and-documentation)

---

## Overview

Google Gemini is a family of multimodal AI models that can process text, images, audio, and video. The Gemini API provides programmatic access to these models for building AI-powered applications.

### Key Features

- **Multimodal capabilities**: Process text, images, audio, and video inputs
- **Multiple model sizes**: From lightweight to highly capable models
- **Streaming support**: Real-time response streaming for better user experience
- **Function calling**: Enable models to call external functions and APIs
- **Safety settings**: Built-in content filtering and safety controls
- **Embeddings**: Generate vector embeddings for semantic search and RAG

### Model Variants

- **Gemini Pro**: General-purpose model for most tasks
- **Gemini Pro Vision**: Optimised for vision and multimodal tasks
- **Gemini Ultra**: Most capable model (when available)
- **Gemini Flash**: Faster, lighter model for quick responses

---

## Getting Started

### Prerequisites

- Google Cloud account
- Billing enabled on your Google Cloud project
- API key or service account credentials

### Quick Setup Steps

1. Create a Google Cloud project or use an existing one
2. Enable the Gemini API in Google Cloud Console
3. Generate an API key or create a service account
4. Install the appropriate SDK for your language
5. Make your first API call

---

## Authentication and API Keys

### API Key Authentication

The simplest authentication method for development and testing.

**Obtaining an API Key:**

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy and securely store your API key

**Using API Keys:**

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
```

**Security Best Practices:**

- Never commit API keys to version control
- Use environment variables or secret management services
- Restrict API key usage by IP address or referrer in Google Cloud Console
- Rotate keys regularly
- Use service accounts for production applications

### Service Account Authentication

For production applications, use service accounts with JSON key files.

```python
from google.oauth2 import service_account
import google.generativeai as genai

credentials = service_account.Credentials.from_service_account_file(
    'path/to/service-account-key.json'
)
genai.configure(credentials=credentials)
```

### OAuth 2.0 Authentication

For user-facing applications that need to access user data.

---

## Available Models

### Model Comparison

| Model | Best For | Input Tokens | Output Tokens | Multimodal |
|-------|----------|--------------|---------------|------------|
| gemini-pro | General text tasks | 32,768 | 2,048 | Text only |
| gemini-pro-vision | Vision and multimodal | 16,384 | 8,192 | Text + Images |
| gemini-1.5-pro | Advanced reasoning | 2M | 8,192 | Text + Images + Audio |
| gemini-1.5-flash | Fast responses | 1M | 8,192 | Text + Images |

### Model Selection Guidelines

- **Text-only tasks**: Use `gemini-pro` or `gemini-1.5-pro`
- **Image analysis**: Use `gemini-pro-vision` or `gemini-1.5-pro`
- **Large context windows**: Use `gemini-1.5-pro` (up to 2M tokens)
- **Speed-critical applications**: Use `gemini-1.5-flash`
- **Complex reasoning**: Use `gemini-1.5-pro`

---

## API Endpoints

### REST API Base URL

```
https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent
```

### gRPC Endpoint

For lower latency and better performance in production environments.

### SDK Endpoints

Each language SDK abstracts the endpoint details. Use SDK methods directly.

---

## Integration Patterns

### Python Integration

**Installation:**

```bash
pip install google-generativeai
```

**Basic Usage:**

```python
import google.generativeai as genai

# Configure API
genai.configure(api_key="YOUR_API_KEY")

# Get model
model = genai.GenerativeModel('gemini-pro')

# Generate content
response = model.generate_content("Explain quantum computing in simple terms")
print(response.text)
```

**Streaming:**

```python
response = model.generate_content(
    "Write a short story about a robot",
    stream=True
)

for chunk in response:
    print(chunk.text, end='')
```

### Node.js/TypeScript Integration

**Installation:**

```bash
npm install @google/generative-ai
```

**Basic Usage:**

```typescript
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.API_KEY!);
const model = genAI.getGenerativeModel({ model: "gemini-pro" });

const result = await model.generateContent("Explain quantum computing");
const response = await result.response;
console.log(response.text());
```

**Streaming:**

```typescript
const result = await model.generateContentStream("Write a story");
for await (const chunk of result.stream) {
    const chunkText = chunk.text();
    process.stdout.write(chunkText);
}
```

### Java Integration

**Maven Dependency:**

```xml
<dependency>
    <groupId>com.google.cloud</groupId>
    <artifactId>google-cloud-aiplatform</artifactId>
    <version>LATEST</version>
</dependency>
```

**Basic Usage:**

```java
import com.google.cloud.aiplatform.v1beta1.*;
import com.google.protobuf.Value;

// Initialize client
VertexAI vertexAI = new VertexAI("project-id", "us-central1");
GenerativeModel model = new GenerativeModel("gemini-pro", vertexAI);

// Generate content
GenerateContentResponse response = model.generateContent(
    "Explain quantum computing"
);
System.out.println(response.getText());
```

### Go Integration

**Installation:**

```bash
go get cloud.google.com/go/aiplatform/apiv1beta1
```

**Basic Usage:**

```go
import (
    aiplatform "cloud.google.com/go/aiplatform/apiv1beta1"
    "cloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb"
)

// Initialize client
ctx := context.Background()
client, err := aiplatform.NewPredictionClient(ctx)
// ... generate content
```

### REST API Direct Integration

**cURL Example:**

```bash
curl \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [{
        "text": "Explain quantum computing"
      }]
    }]
  }' \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_API_KEY"
```

---

## Request and Response Formats

### Request Structure

**Basic Text Request:**

```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "Your prompt here"
        }
      ]
    }
  ]
}
```

**Multimodal Request (Text + Image):**

```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "What's in this image?"
        },
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "base64_encoded_image_data"
          }
        }
      ]
    }
  ]
}
```

**Request with Configuration:**

```json
{
  "contents": [...],
  "generationConfig": {
    "temperature": 0.7,
    "topK": 40,
    "topP": 0.95,
    "maxOutputTokens": 2048,
    "stopSequences": ["STOP"]
  },
  "safetySettings": [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
  ]
}
```

### Response Structure

**Success Response:**

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Generated response text"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "safetyRatings": [...]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 10,
    "candidatesTokenCount": 50,
    "totalTokenCount": 60
  }
}
```

**Error Response:**

```json
{
  "error": {
    "code": 400,
    "message": "Error description",
    "status": "INVALID_ARGUMENT"
  }
}
```

### Generation Configuration Parameters

- **temperature** (0.0-2.0): Controls randomness. Lower = more deterministic
- **topK** (1-40): Limits token selection to top K candidates
- **topP** (0.0-1.0): Nucleus sampling threshold
- **maxOutputTokens**: Maximum tokens in response (1-8192)
- **stopSequences**: Array of strings that stop generation
- **candidateCount**: Number of response candidates (1-8)

### Safety Settings

**Categories:**

- `HARM_CATEGORY_HARASSMENT`
- `HARM_CATEGORY_HATE_SPEECH`
- `HARM_CATEGORY_SEXUALLY_EXPLICIT`
- `HARM_CATEGORY_DANGEROUS_CONTENT`

**Thresholds:**

- `BLOCK_NONE`: Allow all content
- `BLOCK_ONLY_HIGH`: Block only high-risk content
- `BLOCK_MEDIUM_AND_ABOVE`: Block medium and high-risk content
- `BLOCK_LOW_AND_ABOVE`: Block low, medium, and high-risk content

---

## Best Practices

### Prompt Engineering

1. **Be specific and clear**: Vague prompts produce vague results
2. **Provide context**: Include relevant background information
3. **Use examples**: Few-shot learning improves results
4. **Structure your prompts**: Use clear formatting and instructions
5. **Iterate and refine**: Test different phrasings to optimise results

**Example of Good Prompting:**

```
Bad: "Write about AI"

Good: "Write a 500-word article explaining how large language models work, 
targeted at software engineers with basic machine learning knowledge. 
Include examples of transformer architecture and attention mechanisms."
```

### Performance Optimisation

1. **Use streaming**: For better perceived performance in user-facing apps
2. **Cache responses**: Cache common queries to reduce API calls
3. **Batch requests**: When possible, combine multiple requests
4. **Choose the right model**: Use lighter models for simple tasks
5. **Optimise token usage**: Shorter prompts = lower costs and faster responses

### Cost Management

1. **Monitor usage**: Track token consumption regularly
2. **Set budgets**: Configure budget alerts in Google Cloud Console
3. **Optimise prompts**: Reduce unnecessary tokens
4. **Use caching**: Cache frequently requested content
5. **Consider model selection**: Lighter models cost less

### Error Handling

1. **Implement retries**: Use exponential backoff for transient errors
2. **Handle rate limits**: Respect rate limits and implement queuing
3. **Validate inputs**: Check inputs before sending to API
4. **Log errors**: Maintain error logs for debugging
5. **Graceful degradation**: Have fallback mechanisms

### Security

1. **Protect API keys**: Never expose keys in client-side code
2. **Validate outputs**: Don't trust model outputs blindly
3. **Sanitise inputs**: Clean user inputs before sending to API
4. **Use safety settings**: Configure appropriate safety thresholds
5. **Monitor usage**: Watch for unusual patterns that might indicate abuse

---

## Common Use Cases

### 1. Text Generation

**Use Cases:**
- Content creation
- Email drafting
- Code generation
- Creative writing

**Example:**

```python
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(
    "Write a professional email declining a meeting request politely"
)
```

### 2. Text Summarisation

**Use Cases:**
- Article summaries
- Meeting notes
- Document abstracts
- Long-form content compression

**Example:**

```python
long_text = "..." # Your long text
prompt = f"Summarise the following text in 3 bullet points:\n\n{long_text}"
response = model.generate_content(prompt)
```

### 3. Question Answering

**Use Cases:**
- Customer support chatbots
- Knowledge bases
- FAQ systems
- Educational tools

**Example:**

```python
context = "Your knowledge base content..."
question = "What is your return policy?"

prompt = f"Based on the following context, answer the question:\n\nContext: {context}\n\nQuestion: {question}"
response = model.generate_content(prompt)
```

### 4. Image Analysis

**Use Cases:**
- Image description
- OCR and text extraction
- Content moderation
- Visual Q&A

**Example:**

```python
import PIL.Image

img = PIL.Image.open("image.jpg")
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(["What's in this image?", img])
```

### 5. Code Generation and Explanation

**Use Cases:**
- Code completion
- Code review
- Documentation generation
- Bug fixing

**Example:**

```python
code = """
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price
    return total
"""

prompt = f"Review this code and suggest improvements:\n\n{code}"
response = model.generate_content(prompt)
```

### 6. Translation

**Use Cases:**
- Multi-language support
- Content localisation
- Real-time translation

**Example:**

```python
text = "Hello, how are you?"
prompt = f"Translate the following text to French: {text}"
response = model.generate_content(prompt)
```

### 7. Chat Conversations

**Use Cases:**
- Conversational AI
- Virtual assistants
- Interactive applications

**Example:**

```python
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

response = chat.send_message("Hello!")
print(response.text)

response = chat.send_message("What's the weather like?")
print(response.text)
```

### 8. Function Calling

**Use Cases:**
- Tool integration
- API orchestration
- Dynamic workflows

**Example:**

```python
import google.generativeai as genai

# Define functions
weather_function = {
    "name": "get_weather",
    "description": "Get current weather for a location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        }
    }
}

model = genai.GenerativeModel(
    'gemini-pro',
    tools=[weather_function]
)

response = model.generate_content("What's the weather in London?")
# Model can now call the function
```

---

## Error Handling

### Common Error Codes

| Code | Status | Description | Solution |
|------|--------|-------------|----------|
| 400 | INVALID_ARGUMENT | Invalid request parameters | Check request format |
| 401 | UNAUTHENTICATED | Missing or invalid API key | Verify API key |
| 403 | PERMISSION_DENIED | Insufficient permissions | Check API key permissions |
| 429 | RESOURCE_EXHAUSTED | Rate limit exceeded | Implement backoff |
| 500 | INTERNAL | Server error | Retry with exponential backoff |
| 503 | UNAVAILABLE | Service unavailable | Retry after delay |

### Error Handling Pattern

**Python Example:**

```python
import time
import google.generativeai as genai
from google.api_core import retry

def generate_with_retry(prompt, max_retries=3):
    model = genai.GenerativeModel('gemini-pro')
    
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            
            # Exponential backoff
            wait_time = 2 ** attempt
            time.sleep(wait_time)
    
    return None
```

**TypeScript Example:**

```typescript
async function generateWithRetry(
    prompt: string,
    maxRetries: number = 3
): Promise<string> {
    const model = genAI.getGenerativeModel({ model: "gemini-pro" });
    
    for (let attempt = 0; attempt < maxRetries; attempt++) {
        try {
            const result = await model.generateContent(prompt);
            return result.response.text();
        } catch (error) {
            if (attempt === maxRetries - 1) throw error;
            
            const waitTime = Math.pow(2, attempt) * 1000;
            await new Promise(resolve => setTimeout(resolve, waitTime));
        }
    }
    
    throw new Error("Failed after retries");
}
```

### Handling Safety Blocks

```python
response = model.generate_content(prompt)

if response.candidates[0].finish_reason == "SAFETY":
    print("Response blocked by safety filters")
    print(f"Safety ratings: {response.candidates[0].safety_ratings}")
    # Adjust safety settings or prompt
```

---

## Rate Limits and Quotas

### Default Rate Limits

- **Requests per minute**: Varies by model and tier
- **Tokens per minute**: Model-dependent
- **Concurrent requests**: Limited per API key

### Checking Quotas

Monitor usage in Google Cloud Console:
- Navigate to APIs & Services > Quotas
- Filter by "Generative Language API"
- Set up alerts for quota usage

### Handling Rate Limits

1. **Implement exponential backoff**: Wait longer between retries
2. **Queue requests**: Process requests sequentially if needed
3. **Request quota increase**: Contact Google Cloud support
4. **Use multiple API keys**: Distribute load (if allowed by terms)

### Quota Management Code

```python
import time
from collections import deque
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, max_requests=60, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
    
    def wait_if_needed(self):
        now = datetime.now()
        
        # Remove old requests outside time window
        while self.requests and self.requests[0] < now - timedelta(seconds=self.time_window):
            self.requests.popleft()
        
        # If at limit, wait
        if len(self.requests) >= self.max_requests:
            sleep_time = (self.requests[0] + timedelta(seconds=self.time_window) - now).total_seconds()
            time.sleep(sleep_time)
        
        self.requests.append(now)
```

---

## Security Considerations

### API Key Security

1. **Never commit keys**: Use `.gitignore` for key files
2. **Use environment variables**: Store keys in environment variables
3. **Rotate regularly**: Change keys periodically
4. **Restrict usage**: Limit by IP or referrer in Google Cloud Console
5. **Use service accounts**: For production, prefer service accounts

### Input Validation

```python
def validate_input(text: str, max_length: int = 10000) -> bool:
    if not text or not isinstance(text, str):
        return False
    if len(text) > max_length:
        return False
    # Add more validation as needed
    return True
```

### Output Sanitisation

```python
import html

def sanitise_output(text: str) -> str:
    # Escape HTML if displaying in web context
    return html.escape(text)
    
    # Or strip potentially dangerous content
    # return text.replace('<script>', '').replace('</script>', '')
```

### Content Filtering

Always review model outputs before:
- Displaying to users
- Storing in databases
- Using in automated systems
- Making decisions based on outputs

### Privacy Considerations

1. **Don't send PII**: Avoid sending personally identifiable information
2. **Review data policies**: Understand how Google processes your data
3. **Use data residency options**: If available for your region
4. **Implement data retention**: Delete unnecessary data promptly

---

## Code Examples

### Complete Python Example

```python
import google.generativeai as genai
import os
from typing import Optional

class GeminiClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API key required")
        genai.configure(api_key=self.api_key)
    
    def generate_text(
        self,
        prompt: str,
        model: str = "gemini-pro",
        temperature: float = 0.7,
        max_tokens: int = 2048,
        stream: bool = False
    ):
        model_instance = genai.GenerativeModel(model)
        
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
        
        try:
            response = model_instance.generate_content(
                prompt,
                generation_config=generation_config,
                stream=stream
            )
            
            if stream:
                return response
            return response.text
        
        except Exception as e:
            print(f"Error generating content: {e}")
            raise
    
    def chat(
        self,
        messages: list,
        model: str = "gemini-pro"
    ):
        model_instance = genai.GenerativeModel(model)
        chat = model_instance.start_chat(history=[])
        
        for message in messages:
            if message["role"] == "user":
                response = chat.send_message(message["content"])
                messages.append({
                    "role": "assistant",
                    "content": response.text
                })
        
        return messages

# Usage
client = GeminiClient()
response = client.generate_text("Explain machine learning")
print(response)
```

### Complete TypeScript Example

```typescript
import { GoogleGenerativeAI, GenerativeModel, ChatSession } from "@google/generative-ai";

class GeminiClient {
    private genAI: GoogleGenerativeAI;
    private model: GenerativeModel;

    constructor(apiKey?: string) {
        const key = apiKey || process.env.GEMINI_API_KEY;
        if (!key) {
            throw new Error("API key required");
        }
        this.genAI = new GoogleGenerativeAI(key);
        this.model = this.genAI.getGenerativeModel({ model: "gemini-pro" });
    }

    async generateText(
        prompt: string,
        temperature: number = 0.7,
        maxTokens: number = 2048
    ): Promise<string> {
        try {
            const result = await this.model.generateContent({
                contents: [{ role: "user", parts: [{ text: prompt }] }],
                generationConfig: {
                    temperature,
                    maxOutputTokens: maxTokens,
                },
            });

            const response = await result.response;
            return response.text();
        } catch (error) {
            console.error("Error generating content:", error);
            throw error;
        }
    }

    async generateTextStream(
        prompt: string,
        onChunk: (text: string) => void
    ): Promise<void> {
        try {
            const result = await this.model.generateContentStream(prompt);
            
            for await (const chunk of result.stream) {
                const chunkText = chunk.text();
                onChunk(chunkText);
            }
        } catch (error) {
            console.error("Error streaming content:", error);
            throw error;
        }
    }

    startChat(): ChatSession {
        return this.model.startChat({
            history: [],
        });
    }
}

// Usage
const client = new GeminiClient();
const response = await client.generateText("Explain machine learning");
console.log(response);
```

### Multimodal Example (Text + Image)

```python
import google.generativeai as genai
import PIL.Image

# Configure
genai.configure(api_key="YOUR_API_KEY")

# Load image
img = PIL.Image.open("photo.jpg")

# Create model
model = genai.GenerativeModel('gemini-pro-vision')

# Generate with image
response = model.generate_content([
    "Describe what you see in this image in detail",
    img
])

print(response.text)
```

### Function Calling Example

```python
import google.generativeai as genai

# Define function
def get_weather(location: str, unit: str = "celsius") -> str:
    """Get weather for a location (mock function)"""
    return f"Weather in {location}: 22°{unit.upper()[0]}"

# Define function schema
weather_tool = {
    "function_declarations": [
        {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit"
                    }
                },
                "required": ["location"]
            }
        }
    ]
}

# Create model with tools
model = genai.GenerativeModel(
    'gemini-pro',
    tools=[weather_tool]
)

# Generate with function calling
response = model.generate_content("What's the weather in London?")

# Check if function was called
if response.candidates[0].content.parts[0].function_call:
    func_call = response.candidates[0].content.parts[0].function_call
    if func_call.name == "get_weather":
        args = dict(func_call.args)
        result = get_weather(**args)
        print(result)
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: "API key not valid"

**Solutions:**
- Verify API key is correct
- Check API key hasn't been revoked
- Ensure Gemini API is enabled in Google Cloud Console
- Verify billing is enabled

#### Issue: "Rate limit exceeded"

**Solutions:**
- Implement exponential backoff
- Reduce request frequency
- Check quota limits in Google Cloud Console
- Request quota increase if needed

#### Issue: "Model not found"

**Solutions:**
- Verify model name spelling
- Check model availability in your region
- Ensure you're using the correct API version
- Try a different model variant

#### Issue: "Response blocked by safety filters"

**Solutions:**
- Adjust safety settings in request
- Modify prompt to avoid triggering filters
- Review safety ratings in response
- Use appropriate safety thresholds for your use case

#### Issue: "Timeout errors"

**Solutions:**
- Increase timeout settings
- Use streaming for long responses
- Break complex tasks into smaller requests
- Check network connectivity

#### Issue: "Invalid request format"

**Solutions:**
- Verify JSON structure matches API specification
- Check all required fields are present
- Validate data types match expected formats
- Review API documentation for latest changes

### Debugging Tips

1. **Enable logging**: Turn on detailed logging to see request/response details
2. **Test with simple prompts**: Start with basic prompts to isolate issues
3. **Check response metadata**: Review `usageMetadata` and `safetyRatings`
4. **Validate inputs**: Ensure inputs are properly formatted before sending
5. **Monitor API status**: Check Google Cloud status page for outages

### Debugging Code Example

```python
import logging
import google.generativeai as genai

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Configure with detailed error handling
try:
    genai.configure(api_key="YOUR_API_KEY")
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content("Test prompt")
    
    # Log full response details
    print(f"Response text: {response.text}")
    print(f"Finish reason: {response.candidates[0].finish_reason}")
    print(f"Token usage: {response.usage_metadata}")
    print(f"Safety ratings: {response.candidates[0].safety_ratings}")
    
except Exception as e:
    logging.error(f"Error: {e}", exc_info=True)
```

---

## Resources and Documentation

### Official Documentation

- **Google AI Studio**: https://makersuite.google.com/
- **Gemini API Documentation**: https://ai.google.dev/docs
- **Python SDK Reference**: https://ai.google.dev/api/python
- **Node.js SDK Reference**: https://ai.google.dev/api/nodejs
- **REST API Reference**: https://ai.google.dev/api/rest

### Code Samples and Examples

- **GitHub Samples**: https://github.com/google/generative-ai-python
- **Code Examples**: https://ai.google.dev/examples
- **Cookbook**: https://github.com/google/generative-ai-python/tree/main/examples

### Community Resources

- **Google AI Discord**: Community support and discussions
- **Stack Overflow**: Tag `google-generative-ai`
- **Reddit**: r/GoogleAI

### Best Practices Guides

- **Prompt Engineering Guide**: https://ai.google.dev/docs/prompt_intro
- **Safety Best Practices**: https://ai.google.dev/docs/safety_setting_gemini
- **Performance Optimisation**: https://ai.google.dev/docs/performance

### Support

- **Google Cloud Support**: For billing and account issues
- **API Support**: For technical API questions
- **Community Forums**: For general questions and discussions

---

## Quick Reference

### Model Names

- `gemini-pro` - General purpose text model
- `gemini-pro-vision` - Multimodal model
- `gemini-1.5-pro` - Advanced reasoning model
- `gemini-1.5-flash` - Fast response model

### Common Parameters

```python
generation_config = {
    "temperature": 0.7,        # 0.0-2.0
    "topK": 40,                # 1-40
    "topP": 0.95,              # 0.0-1.0
    "maxOutputTokens": 2048,   # 1-8192
    "stopSequences": []        # Array of strings
}
```

### Safety Categories

- `HARM_CATEGORY_HARASSMENT`
- `HARM_CATEGORY_HATE_SPEECH`
- `HARM_CATEGORY_SEXUALLY_EXPLICIT`
- `HARM_CATEGORY_DANGEROUS_CONTENT`

### Safety Thresholds

- `BLOCK_NONE`
- `BLOCK_ONLY_HIGH`
- `BLOCK_MEDIUM_AND_ABOVE`
- `BLOCK_LOW_AND_ABOVE`

---

## Version History

- **v1.0** - Initial comprehensive guide
- Check official documentation for latest API changes and new features

---

**Last Updated**: 2024
**Maintained For**: Professional Gemini AI integration reference

