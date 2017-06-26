from ...models import User 
from .. import main
from ... import cache
from ... import db
from ... import redis_store
from flask import render_template, session, request, jsonify
from ...api import *

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
        session['user'] = {'u_id' : user.u_id, 'name' : user.name, 'email': user.email,'g_id' : user.g_id, 'url' : user.image_url, \
            'aboutme' : user.aboutme}

    return jsonify(json_val)

@main.route('/register', methods=['POST'])
def register():
    name  = request.form['name']
    email = request.form['email']
    passwd = request.form['passwd']

    ret = User.query.filter(db.or_(User.name == name, User.email == email)).all()

    if len(ret) == 2:
        ret_json = {'code' : 3}
    elif len(ret) == 0:
        ret_json = {'code' : 0}
        new_user = User(1, name, email, passwd)
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter(User.email == email).first()
        session['user'] = {'u_id' : user.u_id, 'name' : user.name, 'g_id' : user.g_id, 'url' : user.image_url, \
            'aboutme' : user.aboutme}
    else:
        if name == ret[0].name and email == ret[0].email:
            ret_json = {'code' : 3}
        elif name == ret[0].name:
            ret_json = {'code' : 1}
        elif email == ret[0].email:
            ret_json = {'code' : 2}

    return jsonify(ret_json)




    