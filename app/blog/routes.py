from app.blog import blog
from flask import render_template, abort
from os import path


@blog.route("/blog")
def blog_root_page():
    return render_template("blog.html", page="blog_index.html")


@blog.route("/blog/<blog_page>")
def blog_content_pages(blog_page):
    # Keep a list of valid pages to prevent serving unintended pages
    valid_pages = [
        "DVC and MLflow tutorial.html"
    ]  # Add valid pages here as you add new pages

    if blog_page not in valid_pages:
        abort(404)

    return render_template("blog.html", page="markdown/{}".format(blog_page))
