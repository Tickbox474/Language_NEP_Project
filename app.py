from flask import Flask, request, jsonify
from translate import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        # Parse the JSON request body
        data = request.get_json()
        text = data.get('text', '').strip()       # Get text input by user
        source = data.get('source', 'auto')       # Get source language selected
        target = data.get('target', '')           # Get target language selected

        if not text:
            return jsonify({'error': 'No text provided'}), 400
        if not target:
            return jsonify({'error': 'No target language provided'}), 400

        # Translate the text
        translator = Translator(from_lang=source, to_lang=target)
        translated_text = translator.translate(text)

        return jsonify({'translatedText': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
