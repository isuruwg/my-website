from app.core import core
from flask import render_template


@core.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@core.route('/')
def home_page():
    return render_template('home.html')
