# llm_integration/claude_integration.py
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from config import MODELS, CLAUDE_API_KEY

class ClaudeModel:
    def __init__(self):
        self.model = MODELS['claude']
        self.client = Anthropic(api_key=CLAUDE_API_KEY)

    def generate_response(self, prompt, context=None):
        if context:
            conversation = "\n\n".join([f"{HUMAN_PROMPT if msg['role'] == 'user' else AI_PROMPT} {msg['content']}" for msg in context])
            conversation += f"\n\n{HUMAN_PROMPT} {prompt}"
        else:
            conversation = f"{HUMAN_PROMPT} {prompt}"

        response = self.client.completions.create(
            model=self.model,
            prompt=conversation + AI_PROMPT,
            max_tokens_to_sample=300
        )
        
        return response.completion

    def count_tokens(self, text):
        # Claude doesn't provide a built-in token counter
        # This is a rough estimate, you might want to use a more accurate method
        return len(text.split())
