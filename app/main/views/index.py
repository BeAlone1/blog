from ...models import User 
from .. import main
from ... import cache
from ... import db
from ... import redis_store
from flask import render_template, session, request, jsonify
import pickle
import json
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    
    email = request.form['email']
    passwd = request.form['passwd']

    user = User.query.filter(User.email == email, User.passwd == User.get_md5_passwd(passwd)).first()
    if not user:
        json_val = {"code" : 1, "msg" : "账户或密码错误"}
    else:
        json_val = {"code" : 0, "msg" : user.name}
        session['user'] = {'u_id' : user.u_id, 'name' : user.name, 'g_id' : user.g_id, 'url' : user.image_url, \
            'aboutme' : user.aboutme}

    return jsonify(json_val)

@main.route('/register', methods=['POST'])
def register():
    pass
    