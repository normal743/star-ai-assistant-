from flask import Flask, request, jsonify
from config import MODELS, CONVERSATION_MODES, DEFAULT_MODEL, DEFAULT_MODE
from db_manager import DatabaseManager
from llm_integration import get_llm_instance
from token_counter import count_tokens, calculate_cost, truncate_conversation
from message_formatter import MessageFormatter
from hint_processor import HintProcessor
import logging
from flask_cors import CORS
logging.basicConfig(level=logging.DEBUG)



app = Flask(__name__)
db = DatabaseManager()
hint_processor = HintProcessor()
CORS(app)

@app.before_request
def before_request():
    db.connect()

@app.teardown_request
def teardown_request(exception):
    db.disconnect()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get('user_id')
    message = data.get('message')
    conversation_id = data.get('conversation_id')
    model = data.get('model', DEFAULT_MODEL)
    mode = data.get('mode', DEFAULT_MODE)
    hint = data.get('hint')

    if hint:
        message = hint_processor.process_hint(hint, message)
    else:
        # 如果没有提供 hint，使用当前的模式作为 hint
        message = hint_processor.process_hint(f"mode:{mode}", message)

    llm = get_llm_instance(model)
    formatter = MessageFormatter(model, mode)

    if not conversation_id:
        conversation_id = db.insert_conversation(user_id, model, mode)

    conversation_history = db.get_conversation_history(conversation_id)
    truncated_history = truncate_conversation(conversation_history, model)

    formatted_prompt = formatter.format_prompt(message, truncated_history)
    
    response = llm.generate_response(formatted_prompt)

    input_tokens = count_tokens(formatted_prompt, model)
    output_tokens = count_tokens(response, model)
    cost = calculate_cost(input_tokens, output_tokens, model)

    db.insert_message(conversation_id, 'user', message, input_tokens)
    db.insert_message(conversation_id, 'assistant', response, output_tokens)

    return jsonify({
        'response': response,
        'conversation_id': conversation_id,
        'input_tokens': input_tokens,
        'output_tokens': output_tokens,
        'cost': cost
    })

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Unhandled exception: {str(e)}")
    return jsonify(error=str(e)), 500

# 修改 get_models 和 get_modes 函数
@app.route('/models', methods=['GET'])
def get_models():
    app.logger.info("Accessing /models endpoint")
    try:
        models = list(MODELS.values())
        app.logger.info(f"Returning models: {models}")
        return jsonify(models)
    except Exception as e:
        app.logger.error(f"Error in get_models: {str(e)}")
        return jsonify(error=str(e)), 500

@app.route('/modes', methods=['GET'])
def get_modes():
    app.logger.info("Accessing /modes endpoint")
    try:
        app.logger.info(f"Returning modes: {CONVERSATION_MODES}")
        return jsonify(CONVERSATION_MODES)
    except Exception as e:
        app.logger.error(f"Error in get_modes: {str(e)}")
        return jsonify(error=str(e)), 500

@app.route('/test', methods=['GET'])
def test():
    app.logger.info("Accessing /test endpoint")
    return "Test successful", 200

if __name__ == '__main__':
    db.connect()
    db.create_tables()
    app.run(debug=True,port=5001)
