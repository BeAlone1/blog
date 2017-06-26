from flask import render_template, request, session, redirect
from .. import auth
from ... import cache
from ... import db
from datetime import datetime
from ... import redis_store
from ...models import *

@auth.route('/user')
def user_index():
    return render_template('bloglist.html')

@auth.route('/addblog', methods = ['GET', 'POST'])
def addblog():
    
    u_id = session['user']['u_id']
    if request.method == "GET":
        return render_template('edit.html')
    
    title = request.form['title']
    content = request.form['content']

    arti = Article(u_id = u_id ,title = title, content = content, read_num = 0)
    try:
        db.session.add(arti)
        db.session.commit()

        redis_store.hmset('article_' + str(arti.arti_id)), {'u_id': u_id , 'u_name': session['user']['name'], \
            'title': title, 'content': content, \
            'read_num': 0, 'comment_num': 0, 'uptime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    except:
        return "has error"
    else:
        return redirect('/user')
