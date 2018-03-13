import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__) # load config 

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Database functions
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new db connection if none exists in context"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Close db again after request"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    """initializes db from schema file"""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb') # allows command line usage of function
def initdb_command():
    """Initialiazes db"""
    init_db()
    print('Initialiazed the database.')

# App route functions
@app.route('/')
def hello_world():
    welcome_message = 'Welcome! This API helps retrieve and save simple notes stored as files.'
    return render_template('welcome_page.html', message=welcome_message)

@app.route('/note', methods=['GET', 'POST'])
def new_note():
    if request.method == 'GET':
        return render_template('notes_page.html')

    if request.method == 'POST':
        return render_template('notes_page.html', note_name="a thing!", note_body="another thing!")

@app.route('/note/<name>')
def get_note_with_name(name):
    response = "{}".format(name)

    return render_template('notes_page.html', text=response)

@app.route('/note')
def get_a_list_of_notes():
    return 'A list of notes!'