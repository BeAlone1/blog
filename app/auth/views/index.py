from flask import render_template, request, session
from .. import auth
from ... import cache
from ... import db
from ... import redis_store

@auth.route('/user')
def user_index():
    return render_template('user.html')
