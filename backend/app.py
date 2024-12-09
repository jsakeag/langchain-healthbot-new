from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from chatbot import chatbot_response

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['OPTIONS', 'POST'])
#@cross_origin
def chat():
    # Handle preflight request
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response, 204
    
    # Handle POST request
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    # Get the response from the chatbot
    response = chatbot_response(user_input)
    
    # Create response with CORS headers
    response_json = make_response(jsonify({"response": response}))
    response_json.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response_json

if __name__ == '__main__':
    app.run(debug=True)