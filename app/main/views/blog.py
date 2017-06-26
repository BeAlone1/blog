from ...models import User 
from .. import main
from ... import cache
from ... import db
from ... import redis_store
from flask import render_template, session, request
from ...api import *

@main.route('/blog/<int:art_id>', methods = ['GET'])
def showblog(art_id):
    return get_blog(art_id)