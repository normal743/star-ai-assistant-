# llm_integration/ollama_integration.py
import requests
from config import MODELS
import json

class OllamaModel:
    def __init__(self):
        self.model = MODELS['ollama']
        self.api_url = "http://localhost:11434/api/generate"

    def generate_response(self, prompt, context=None):
        data = {
            "model": self.model,
            "prompt": prompt,
            "context": context if context else []
        }
        
        response = requests.post(self.api_url, json=data, stream=True)
        
        if response.status_code == 200:
            full_response = ""
            for line in response.iter_lines():
                if line:
                    chunk = line.decode('utf-8')
                    # Parse the JSON chunk
                    chunk_data = json.loads(chunk)
                    full_response += chunk_data.get('response', '')
                    if chunk_data.get('done', False):
                        break
            return full_response
        else:
            raise Exception(f"Error from Ollama API: {response.text}")

    def count_tokens(self, text):
        # Ollama doesn't provide a built-in token counter
        # This is a rough estimate, you might want to use a more accurate method
        return len(text.split())
