# blawgh.py -- A simple blog engine, web interface
# Author: Baishampayan Ghose <b.ghose@infinitelybeta.com>
# License: Public domain

from flask import Flask, render_template, request, redirect, url_for
from utils import backend

blawgh = Flask(__name__)

@blawgh.route("/")
def index():
    """Render the index page
    """
    posts = backend.fetch_posts()
    return render_template("index.html", title="Blawgh!", posts=posts)


@blawgh.route("/posts/", methods=("POST",))
def create_post():
    """Create a new post
    """
    import pdb; pdb.set_trace()
    author_email = request.form["author_email"]
    title = request.form["title"]
    body = request.form["body"]
    tags = request.form["tags"].split(",")
    
    new_post = backend.create_post(author_email, title, body, tags)
    if new_post:
        post_url = url_for("show_post", post_id=str(new_post))
        return redirect(post_url)
    return redirect(url_for("index"))


@blawgh.route("/posts/<post_id>/comments/", methods=("POST",))
def create_comment(post_id):
    """Create a new comment
    """
    author = request.form["author"]
    email = request.form["email"]
    body = request.form["body"]

    comment = backend.insert_comment(post_id, author, email, body)
    post_url = url_for("show_post", post_id=str(post_id))
    return redirect(post_url)


@blawgh.route("/posts/<post_id>/")
def show_post(post_id):
    """Render a single post
    """
    post = backend.fetch_post_by_id(post_id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    blawgh.run(debug=True)
