from .ollama_integration import OllamaModel
from .openai_integration import OpenAIModel
from .claude_integration import ClaudeModel
from config import MODELS

def get_llm_instance(model_name):
    if model_name == MODELS['ollama']:
        return OllamaModel()
    elif model_name == MODELS['openai']:
        return OpenAIModel()
    elif model_name == MODELS['claude']:
        return ClaudeModel()
    else:
        raise ValueError(f"Unknown model: {model_name}")
