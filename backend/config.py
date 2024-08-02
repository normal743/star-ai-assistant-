import os

# LLM Models
MODELS = {
    'ollama': 'llama3.1:8b',
    'openai': 'gpt-4o-mini',
    'claude': 'claude-3-5-sonnet-20240620'
}

# Token Prices (in dollars per million tokens)
TOKEN_PRICES = {
    'gpt-4o': {'input': 5, 'output': 15},
    'claude-3-5-sonnet-20240620': {'input': 3, 'output': 15},
    'llama3.1:7b': {'input': 0, 'output': 0}  # Ollama is free
}

# 在 config.py 中添加：

MODE_PROMPTS = {
    'normal': "Respond to user queries in a friendly and informative manner.",
    'python_execution': "When asked about Python, provide code examples and explain how to execute them. If asked to run Python code, use the provided Python execution environment.",
    'developer': "Provide detailed technical explanations and code snippets when appropriate. Focus on best practices and efficient solutions.",
    'teaching': "Explain concepts in detail, providing examples and analogies to aid understanding. Adjust your explanations based on the user's level of knowledge.",
    'creative': "Provide innovative and out-of-the-box ideas and solutions. Encourage creative thinking and unique approaches.",
    'concise': "Provide brief and to-the-point responses. Focus on the most important information and avoid unnecessary details."
}


# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

# Default Settings
DEFAULT_MODEL = 'ollama'
DEFAULT_MODE = 'normal'

# Conversation Modes
CONVERSATION_MODES = [
    'normal',
    'python_execution',
    'developer',
    'teaching',
    'creative',
    'concise'
]

# Token Limits
MAX_TOKENS = 128000  # 128k tokens

# Database Configuration
DB_CONFIG = {
       'host': 'localhost',
       'user': 'star_user',
       'password': 'Star743',
       'database': 'star_ai_assistant'
   }
   

# Other Settings
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
