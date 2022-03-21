from app.blog import blog
from flask import render_template


@blog.route("/blog")
def blog_root_page():
    return render_template("blog.html")
