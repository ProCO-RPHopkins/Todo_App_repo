# Run this at the beginning of each flask 
# Activate the virtual environment python -m venv .venv
#URL: http://127.0.0.1:5000/

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)