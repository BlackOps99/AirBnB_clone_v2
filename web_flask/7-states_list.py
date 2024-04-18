#!/usr/bin/python3
"""
start the web application using Flask
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    dict_states = storage.all(State)
    all_states = []
    for k, v in dict_states.items():
        all_states.append(v)
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
