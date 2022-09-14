#!/usr/bin/python3
""" Script that starts a Flask web application """

from logging import exception
from os import stat_result
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """states
    Function that displays a HTML page with a list of all
    State objects from a database
    """
    states = storage.all("State")
    if state_id is not None:
        state = 'State.' + state_id
        return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes the storage on teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
