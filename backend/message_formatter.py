from config import CONVERSATION_MODES, MODELS

class MessageFormatter:
    def __init__(self, model, mode):
        self.model = model
        self.mode = mode

    def format_system_message(self):
        base_instruction = "You are a helpful AI assistant named Star."
        mode_instructions = {
            'normal': "Respond to user queries in a friendly and informative manner.",
            'python_execution': "When asked about Python, provide code examples and explain how to execute them.",
            'developer': "Provide detailed technical explanations and code snippets when appropriate.",
            'teaching': "Explain concepts in detail, providing examples and analogies to aid understanding.",
            'creative': "Provide innovative and out-of-the-box ideas and solutions.",
            'concise': "Provide brief and to-the-point responses."
        }
        
        instruction = f"{base_instruction} {mode_instructions.get(self.mode, mode_instructions['normal'])}"
        
        if self.model == MODELS['ollama']:
            return instruction
        elif self.model == MODELS['openai']:
            return {"role": "system", "content": instruction}
        elif self.model == MODELS['claude']:
            return f"Human: {instruction}\n\nAssistant: Understood. I'll act as Star, a helpful AI assistant, and follow the given instructions for our conversation. How can I assist you today?"
        else:
            raise ValueError(f"Unknown model: {self.model}")

    def format_user_message(self, content):
        if self.model == MODELS['ollama']:
            return content
        elif self.model == MODELS['openai']:
            return {"role": "user", "content": content}
        elif self.model == MODELS['claude']:
            return f"Human: {content}"
        else:
            raise ValueError(f"Unknown model: {self.model}")

    def format_assistant_message(self, content):
        if self.model == MODELS['ollama']:
            return content
        elif self.model == MODELS['openai']:
            return {"role": "assistant", "content": content}
        elif self.model == MODELS['claude']:
            return f"Assistant: {content}"
        else:
            raise ValueError(f"Unknown model: {self.model}")

    def format_conversation(self, messages):
        formatted_messages = []
        for message in messages:
            if message['role'] == 'user':
                formatted_messages.append(self.format_user_message(message['content']))
            elif message['role'] == 'assistant':
                formatted_messages.append(self.format_assistant_message(message['content']))
        
        if self.model == MODELS['claude']:
            return "\n\n".join(formatted_messages)
        else:
            return formatted_messages

    def format_prompt(self, user_input, conversation_history=None):
        if conversation_history is None:
            conversation_history = []
        
        system_message = self.format_system_message()
        formatted_history = self.format_conversation(conversation_history)
        user_message = self.format_user_message(user_input)
        
        if self.model == MODELS['ollama']:
            prompt = f"{system_message}\n\n"
            prompt += "\n\n".join(formatted_history)
            prompt += f"\n\n{user_message}"
            return prompt
        elif self.model == MODELS['openai']:
            messages = [system_message] + formatted_history + [user_message]
            return messages
        elif self.model == MODELS['claude']:
            prompt = f"{system_message}\n\n"
            prompt += formatted_history
            prompt += f"\n\n{user_message}\n\nAssistant:"
            return prompt
        else:
            raise ValueError(f"Unknown model: {self.model}")

# Usage example:
# formatter = MessageFormatter(MODELS['openai'], 'normal')
# conversation_history = [
#     {"role": "user", "content": "Hello, how are you?"},
#     {"role": "assistant", "content": "I'm doing well, thank you for asking. How can I assist you today?"},
# ]
# user_input = "Can you explain what machine learning is?"
# formatted_prompt = formatter.format_prompt(user_input, conversation_history)
# print(formatted_prompt)
