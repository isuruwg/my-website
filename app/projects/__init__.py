from flask import Blueprint

projects = Blueprint("projects", __name__, template_folder="templates")

from app.projects import routes
