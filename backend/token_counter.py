import tiktoken
from config import TOKEN_PRICES, MODELS
from llm_integration import get_llm_instance

def get_encoder(model):
    if model == MODELS['openai']:
        return tiktoken.encoding_for_model(model)
    elif model == MODELS['claude']:
        return tiktoken.get_encoding("cl100k_base")
    else:  # For Ollama or other models
        return None

def count_tokens(text, model):
    encoder = get_encoder(model)
    if encoder:
        return len(encoder.encode(text))
    else:
        # For models without a specific encoder, use the model's count_tokens method
        llm = get_llm_instance(model)
        return llm.count_tokens(text)

def calculate_cost(input_tokens, output_tokens, model):
    if model not in TOKEN_PRICES:
        return 0  # Free models like Ollama

    price = TOKEN_PRICES[model]
    input_cost = (input_tokens / 1_000_000) * price['input']
    output_cost = (output_tokens / 1_000_000) * price['output']
    return input_cost + output_cost

def estimate_total_tokens(conversation, model):
    total_tokens = 0
    for message in conversation:
        total_tokens += count_tokens(message['content'], model)
    return total_tokens

def get_max_tokens(model):
    if model == MODELS['openai']:
        return 8192  # GPT-4 8k context window
    elif model == MODELS['claude']:
        return 100000  # Claude 100k context window
    else:
        return 4096  # Default for other models, adjust as needed

def truncate_conversation(conversation, model, max_new_tokens=1000):
    max_tokens = get_max_tokens(model) - max_new_tokens
    truncated_conversation = []
    total_tokens = 0

    for message in reversed(conversation):
        message_tokens = count_tokens(message['content'], model)
        if total_tokens + message_tokens > max_tokens:
            break
        truncated_conversation.insert(0, message)
        total_tokens += message_tokens

    return truncated_conversation

# Usage example:
# model = MODELS['openai']
# conversation = [
#     {"role": "user", "content": "Hello, how are you?"},
#     {"role": "assistant", "content": "I'm doing well, thank you for asking. How can I assist you today?"},
# ]
# input_tokens = estimate_total_tokens(conversation, model)
# output_tokens = count_tokens("This is a sample response.", model)
# cost = calculate_cost(input_tokens, output_tokens, model)
# print(f"Estimated cost: ${cost:.6f}")
