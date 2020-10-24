from app.projects import projects
from flask import render_template


@projects.route("/projects")
def projects_page():
    return render_template("projects.html")
