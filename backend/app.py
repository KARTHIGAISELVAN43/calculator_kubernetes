from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def evaluate_expression(expression):
    try:
        # Sanitize input: allow only numbers, operators, and decimal points
        if not re.match(r'^[\d+\-*/.() ]+$', expression):
            return None
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except:
        return None

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    result = evaluate_expression(expression)
    if result is None:
        return jsonify({'error': 'Invalid expression'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)