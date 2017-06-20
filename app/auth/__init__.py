from flask import Blueprint, session, redirect

auth = Blueprint('auth', __name__)

from .views import index

@auth.before_request
def has_login():
    if not session.get('user'):
        return redirect('/')