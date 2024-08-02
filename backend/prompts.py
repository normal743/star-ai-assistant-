from config import CONVERSATION_MODES, MODELS

class PromptManager:
    @staticmethod
    def get_system_prompt(model, mode):
        base_prompt = "You are Star, an AI assistant created by Anthropic to be helpful, harmless, and honest."
        
        mode_prompts = {
            'normal': "Respond to user queries in a friendly and informative manner.",
            'python_execution': "When asked about Python, provide code examples and explain how to execute them. If asked to run Python code, use the provided Python execution environment.",
            'developer': "Provide detailed technical explanations and code snippets when appropriate. Focus on best practices and efficient solutions.",
            'teaching': "Explain concepts in detail, providing examples and analogies to aid understanding. Adjust your explanations based on the user's level of knowledge.",
            'creative': "Provide innovative and out-of-the-box ideas and solutions. Encourage creative thinking and unique approaches.",
            'concise': "Provide brief and to-the-point responses. Focus on the most important information and avoid unnecessary details."
        }
        
        model_specific_instructions = {
            MODELS['ollama']: "You are running on an Ollama model.",
            MODELS['openai']: "You are running on an OpenAI model.",
            MODELS['claude']: "You are running on an Anthropic Claude model."
        }
        
        prompt = f"{base_prompt} {mode_prompts.get(mode, mode_prompts['normal'])} {model_specific_instructions.get(model, '')}"
        return prompt

    @staticmethod
    def get_user_prompt(mode, user_input):
        mode_prefixes = {
            'normal': "",
            'python_execution': "I have a Python-related question or task: ",
            'developer': "As a developer, I need help with: ",
            'teaching': "Could you explain this concept to me: ",
            'creative': "I'm looking for creative ideas about: ",
            'concise': "In brief, "
        }
        
        prefix = mode_prefixes.get(mode, "")
        return f"{prefix}{user_input}"

# Usage example:
# system_prompt = PromptManager.get_system_prompt(MODELS['openai'], 'teaching')
# user_prompt = PromptManager.get_user_prompt('teaching', "What is quantum computing?")
# print(system_prompt)
# print(user_prompt)
