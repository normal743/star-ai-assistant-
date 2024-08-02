# llm_integration/openai_integration.py
import openai
from config import MODELS, OPENAI_API_KEY

class OpenAIModel:
    def __init__(self):
        self.model = MODELS['openai']
        openai.api_key = OPENAI_API_KEY

    def generate_response(self, prompt, context=None):
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        
        if context:
            messages.extend(context)
        
        messages.append({"role": "user", "content": prompt})
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )
        
        return response.choices[0].message['content']

    def count_tokens(self, text):
        return len(openai.Completion.create(
            model="text-davinci-002",
            prompt=text,
            max_tokens=0
        )["usage"]["prompt_tokens"])
