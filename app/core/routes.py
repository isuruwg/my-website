from app.core import core
from flask import render_template

@core.route('/')
def home_page():
    return render_template('home.html')
