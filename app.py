from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json  # Get the JSON data from the request
    text = data.get('text')  # Extract the text to be translated
    source = data.get('source')  # Extract the source language code
    target = data.get('target')  # Extract the target language code

    if not text or not target:
        return jsonify({'error': 'Invalid input'}), 400  # Handle missing input

    try:
        # Translate the text using googletrans (might be the problem here)
        translation = translator.translate(text, src=source, dest=target)
        return jsonify({'translatedText': translation.text})  # Send back the translated text
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Handle any errors

if __name__ == '__main__':
    app.run(debug=True)
