# backend.py -- A simple blog engine using MongoDB
# Author: Baishampayan Ghose <b.ghose@infinitelybeta.com>
# License: Public domain

from pymongo import Connection, DESCENDING  # MongoDB client
from datetime import datetime   # Date library
from bson.objectid import ObjectId       # Needed later

DB_NAME = "blog"
USERS_COLLECTION_NAME = "users"
POSTS_COLLECTION_NAME = "posts"

# Need to create these once
CONNECTION = Connection("localhost", 27017) # All default
DB = CONNECTION[DB_NAME]
USERS_COLLECTION = DB[USERS_COLLECTION_NAME]
POSTS_COLLECTION = DB[POSTS_COLLECTION_NAME]

# User fields
# username, full_name, email, joined_on

# Post fields
# author_id, title, body, created_at, comments, tags

# Comment fields (embedded)
# author, email, body, posted_at


# Create a new user
def create_user(username, full_name, email):
    """Create a new user account
    """
    return USERS_COLLECTION.insert({"username": username,
                                    "full_name": full_name,
                                    "email": email, # needs to be unique in the real world
                                    "joined_on": datetime.utcnow()})


# Get an existing user
def get_user(email):
    """Retrieve a user account using its email address
    """
    return USERS_COLLECTION.find_one({"email": email})


# import re
# R_TITLE = re.compile(r"[^a-zA-Z0-9]+")

# def slugify(title):
#     """Slugify a title
#     """
#     return R_TITLE.sub("-", title.lower()).strip("-")

# Create post
def create_post(author_email, title, body, tags=[]):
    """Create a new post
    """
    author = get_user(author_email) # fetch author info

    if author:
        return POSTS_COLLECTION.insert({"author_id": author[u"_id"],
                                        "author_name": author[u"full_name"],
                                        "title": title,
                                        "body": body,
                                        "created_at": datetime.utcnow(),
                                        "comments": [], # no comments to begin with
                                        "tags": tags})
    return None


# Fetch all posts
def fetch_posts():
    """Fetch all the posts ordered by date time
    """
    cur = POSTS_COLLECTION.find({}) # get the cursor
    cur.sort("created_at", DESCENDING) # sort by datetime
    return [post for post in cur]      # realise the iterable


# Fetch post by given Id
def fetch_post_by_id(id_str):
    """Fetch a given post by its Id
    """
    return POSTS_COLLECTION.find_one({"_id": ObjectId(id_str)})


# Insert comment
def insert_comment(post_id, author, email, body):
    """Insert a new comment into a post
    """
    comment_doc = {"author": author,
                   "email": email,
                   "body": body,
                   "posted_at": datetime.utcnow()}
    
    return POSTS_COLLECTION.update({"_id": ObjectId(post_id)}, # find the post
                                   {"$push": {"comments": comment_doc}}) # push to array


if __name__ == "__main__":
    pass
    
