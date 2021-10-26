# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT  # Flask is the web app that we will customize
from flask import Flask 
from flask import render_template
from flask import request
from flask import redirect, url_for 

app = Flask(__name__)     # create an app

notes = {1: {'title': 'First note', 'text': 'This is my first note', 'date': '10-1-2020'}, 2: {'title': 'Second note', 'text': 'This is my second note', 'date': '10-2-2020'}, 3: {'title': 'Third note', 'text': 'This is my third note', 'date': '10-3-2020'} }

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/index')
def index():
    a_user = {'name': 'Justin', 'email':'jleiner1@uncc.edu'}

    return render_template('index.html', user = a_user)

@app.route('/notes')
def get_notes():
    a_user = {'name': 'Justin', 'email':'jleiner1@uncc.edu'}

    return render_template('notes.html', notes = notes, user = a_user)

@app.route('/notes/<note_id>')
def get_note(note_id):
    
    a_user = {'name': 'Justin', 'email':'jleiner1@uncc.edu'}

    return render_template('note.html', note = notes[int(note_id)], user = a_user)

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    a_user = {'name': 'Justin', 'email':'jleiner1@uncc.edu'}

    if request.method == 'POST':
        
        # Get title data
        title = request.form['title']

        # Get note data
        text = request.form['noteText']

        # Create date stamp
        from datetime import date
        today = date.today()

        # Date format
        today = today.strftime("%m-%d-%Y")

        # Get the last id used and increment it by 1
        id = len(notes) + 1

        # Creates new note entry
        notes[id] = {'title': title, 'text': text, 'date': today}

        return redirect(url_for('get_notes', name = a_user))
    else:
        return render_template('new.html', user = a_user)

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.