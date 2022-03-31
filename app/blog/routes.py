from app.blog import blog
from flask import render_template


@blog.route("/blog")
def blog_root_page():
    return render_template("blog.html", page="blog_index.html")


@blog.route("/blog/<blog_page>")
def blog_content_pages(blog_page):
    return render_template("blog.html", page="markdown/{}".format(blog_page))
