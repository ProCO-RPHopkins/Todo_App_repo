# Run this at the beginning of each flask 
# Activate the virtual environment python -m venv .venv
#URL: http://127.0.0.1:5000/

# building a to-do list app tomorrow
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask, how are you!'

@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/user/<username>')
def show_user_profile(username):
    username = 'Ryan'
    return f'User {username}'

@app.route('/post/<post_id>')
def show_post(post_id):
    post_id = 'This is the first post to my app. Welcome to InVeXodus!'
    return post_id

@app.route('/hello/<name>')
def show_subpath(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run() 