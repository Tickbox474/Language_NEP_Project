from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def upload_form():
    return render_template('upload_form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the form.'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected.'
    
    # Save the file to the upload folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    return f'File {file.filename} uploaded successfully.'

if __name__ == "__main__":
    app.run(debug=True)
