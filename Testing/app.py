from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route to serve the index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle translation requests
@app.route('/translate', methods=['POST'])
def handle_translation():  # Renamed function to avoid conflict
    data = request.get_json()
    text = data.get('text')
    target_lang = data.get('target_language')

    try:
        # Use TextBlob for translation
        blob = TextBlob(text)
        translated_text = str(blob.translate(to=target_lang))

        # Return the translated text in a JSON format
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        # Handle any translation errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
