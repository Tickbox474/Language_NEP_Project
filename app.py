from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle translation
@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    source_lang = data.get('source_language')
    target_lang = data.get('target_language')
    
    if not text or not target_lang:
        return jsonify({'error': 'Missing text or target language'}), 400

    # Perform translation
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    
    # Return the translated text as JSON
    return jsonify({'translated_text': translation.text})

if __name__ == '__main__':
    app.run(debug=True)
