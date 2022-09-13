#!/usr/bin/python3
""" 7-states_list.py
Module that starts a Flask web application
and lists all State instances from a database
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
