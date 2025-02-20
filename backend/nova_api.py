from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/ask', methods=['POST'])
def ask_nova():
    data = request.json
    user_input = data.get("question", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are NOVA, an advanced AI assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
