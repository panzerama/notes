from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome!'

@app.route('/note/<name>')
def get_note_with_name(name):
    return 'Retrieve node {}'.format(name)

@app.route('/notes/<pagename>')
def a_particular_note_page(pagename):
    return '{}'.format(pagename)
