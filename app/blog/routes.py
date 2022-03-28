from app.blog import blog
from flask import render_template, abort
from os import path


@blog.route("/blog")
def blog_root_page():
    return render_template("blog.html", page="blog_index.html")


@blog.route("/blog/<blog_page>")
def blog_content_pages(blog_page):
    # create the path for the page
    page_path = "markdown/{}".format(blog_page)
    if not path.isfile(page_path):
        abort(404)

    return render_template("blog.html", page=page_path)
