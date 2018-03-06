from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome! This API helps retrieve and save simple notes stored as files.'

@app.route('/note/<name>')
def get_note_with_name(name):
    return 'Retrieve node {}'.format(name)

@app.route('/note')
def get_a_list_of_notes():
    return 'A list of notes!'
