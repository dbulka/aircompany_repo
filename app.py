"""
    This module contains web service methods for app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<a href='/hijack'> HI </a>"

