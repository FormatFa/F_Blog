from flask import render_template,request,redirect,url_for

from . import blue_posts
from . import logger


@blue_posts.route('/')
def index():
    return render_template('posts/index.html',name='posts')




