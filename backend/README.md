# Star AI Assistant

## English Introduction

Star AI Assistant is a versatile and powerful AI chatbot system that integrates multiple language models (LLMs) including Ollama, OpenAI, and Claude. It offers various conversation modes, Python code execution capabilities, and a hint system for fine-tuned responses.

### Key Features:
- Multi-model support (Ollama, OpenAI, Claude)
- Multiple conversation modes
- Python code execution environment
- Token counting and cost calculation
- Conversation history storage using MySQL
- Hint system for guiding AI responses

### Setup and Installation:
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (API keys, database credentials)
4. Run the application: `python app.py`

## 中文介绍

Star AI 助手是一个多功能且强大的 AI 聊天机器人系统，集成了多个语言模型（LLM），包括 Ollama、OpenAI 和 Claude。它提供多种对话模式、Python 代码执行功能，以及用于精确调整响应的提示系统。

### 主要特点：
- 多模型支持（Ollama、OpenAI、Claude）
- 多种对话模式
- Python 代码执行环境
- Token 计数和成本计算
- 使用 MySQL 存储对话历史
- 用于引导 AI 响应的提示系统

### 设置和安装：
1. 克隆仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 设置环境变量（API 密钥、数据库凭证）
4. 运行应用：`python app.py`

## Project Structure and Functionality

### Directory Structure:
star-ai-assistant/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── db_manager.py
│   ├── hint_processor.py
│   ├── message_formatter.py
│   ├── prompts.py
│   ├── python_executor.py
│   ├── token_counter.py
│   ├── llm_integration/
│   │   ├── init.py
│   │   ├── ollama_integration.py
│   │   ├── openai_integration.py
│   │   └── claude_integration.py
│   ├── requirements.txt
│   └── README.md

### File Descriptions and Functionalities:

1. **app.py**
   - Main Flask application file
   - Handles API routes and integrates all components
   - Provides endpoints for chat, model selection, and conversation modes

2. **config.py**
   - Contains configuration settings, API keys, and constants
   - Defines available models, token prices, and conversation modes
   - Centralizes MODE_PROMPTS for use across the application

3. **db_manager.py**
   - Manages database connections and operations
   - Handles conversation and message storage in MySQL

4. **hint_processor.py**
   - Processes user-provided hints to guide AI responses
   - Supports various hint types: tone, length, focus, style, expertise, and status
   - Integrates with MODE_PROMPTS for consistent conversation modes

5. **message_formatter.py**
   - Formats messages for different LLM models and conversation modes
   - Ensures consistent message structure across different models

6. **prompts.py**
   - Manages system and user prompts
   - Generates appropriate prompts based on selected model and conversation mode

7. **python_executor.py**
   - Provides a safe environment for executing Python code
   - Captures output, errors, and returned values from code execution

8. **token_counter.py**
   - Counts tokens for input and output messages
   - Calculates costs based on token usage and model pricing
   - Handles conversation truncation to meet model token limits

9. **llm_integration/**
   - Contains model-specific integration files
   - **__init__.py**: Provides a unified interface for different LLM models
   - **ollama_integration.py**: Handles interactions with the Ollama API
   - **openai_integration.py**: Manages OpenAI API interactions
   - **claude_integration.py**: Facilitates Claude API interactions

### Key Functionalities:

1. **Multi-Model Support**
   - Seamlessly switch between Ollama, OpenAI, and Claude models
   - Model-specific message formatting and API interactions

2. **Conversation Modes**
   - Supports multiple modes: normal, python_execution, developer, teaching, creative, concise
   - Each mode provides tailored AI responses and behavior

3. **Hint System**
   - Allows users to guide AI responses with specific hints
   - Supports tone, length, focus, style, expertise, and status hints
   - Integrates with conversation modes for consistent behavior

4. **Python Code Execution**
   - Safe execution of Python code within the chat environment
   - Captures and returns output, errors, and execution results

5. **Token Management**
   - Accurate token counting for different models
   - Cost calculation based on token usage and model-specific pricing
   - Conversation truncation to meet model token limits

6. **Database Integration**
   - Stores conversation history and messages in MySQL
   - Allows for conversation continuity and analysis

7. **Flexible Configuration**
   - Centralized configuration management in config.py
   - Easy customization of models, modes, and system behavior

This structure provides a flexible and extensible foundation for the Star AI Assistant, allowing for easy addition of new models, conversation modes, and features in the future.
