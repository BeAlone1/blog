from . import db
from hashlib import md5
from datetime import datetime
from sqlalchemy.dialects.mysql import INTEGER

class User(db.Model):
    __tablename__ = 'user'

    u_id = db.Column(INTEGER(unsigned = True), primary_key = True)
    g_id = db.Column(INTEGER(unsigned = True), nullable = False, server_default = '1')
    name = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(45), nullable = False, unique = True)
    passwd = db.Column(db.String(32), nullable = False)
    phonenum = db.Column(db.String(12))
    image_url = db.Column(db.String(200))
    aboutme = db.Column(db.String(500))
    create_time = db.Column(db.DateTime)

    def __init__(self, g_id, name, email, passwd, create_time = None):
        self.g_id = g_id
        self.name = name
        self.email = email
        self.passwd = self.get_md5_passwd(passwd)
        if not create_time:
            self.create_time = datetime.now()

    @staticmethod
    def get_md5_passwd(passwd):
        m = md5()
        m.update(passwd.encode())
        return m.hexdigest()

    def __repr__(self):
        return '<User(%d, %d, %s, %s, %s, %s)>' %(self.u_id, self.g_id, self.name, self.email \
            ,self.image_url, self.aboutme)

class Article(db.Model):
    __tablename__ = 'article'

    arti_id = db.Column(INTEGER(unsigned = True), primary_key = True)
    u_id = db.Column(INTEGER(unsigned = True), db.ForeignKey('user.u_id'))
    title = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text, nullable = False)
    read_num = db.Column(INTEGER(unsigned = True), default = 0)
    uptime = db.Column(db.DateTime, nullable = False)

    def __init__(self, u_id, title, content, read_num = 0, uptime = None):
        self.u_id = u_id
        self.title = title
        self.read_num = read_num
        self.content = content
        if not uptime:
            self.uptime = datetime.now()

    def __repr__(self):
        return '<Article(%d, %d, %s, %d, %s)>' % (self.arti_id, self.u_id, self.title, \
            self.read_num, self.update.strftime('%Y-%m-%d %H:%M:%S'))

class Follow(db.Model):
    __tablename__ = 'follow'

    f_id = db.Column(INTEGER(unsigned = True), primary_key = True)
    u_id = db.Column(INTEGER(unsigned = True), db.ForeignKey('user.u_id'))
    follow_id = db.Column(INTEGER(unsigned = True), db.ForeignKey('user.u_id'))

    def __init__(self, u_id, follow_id):
        self.u_id = u_id
        self.follow_id = follow_id

    def __repr__(self):
        return '<Follow(%d, %d)>' % (self.f_id, self.follow_id)

class Comment(db.Model):
    __tablename__ = 'comment'

    com_id = db.Column(INTEGER(unsigned = True), primary_key = True)
    f_com_id = db.Column(INTEGER(unsigned = True), db.ForeignKey('comment.com_id'))
    u_id = db.Column(INTEGER(unsigned = True), db.ForeignKey('user.u_id'))
    arti_id = db.Column(INTEGER(unsigned = True), db.ForeignKey('article.arti_id'))
    com_content = db.Column(db.Text, nullable = False)
    com_time = db.Column(db.DateTime, nullable = False)

    def __init__(self, f_com_id, u_id, arti_id, com_content, com_time):
        self.f_com_id = f_com_id
        self.u_id = u_id
        self.arti_id = arti_id
        self.com_content = com_content
        self.com_time = datetime.now()
    
    def __repr__(self):
        return '<Comment(%d, %d, %d, %d, %s, %s)>' % (self.com_id, self.f_com_id, self.u_id \
            , self.arti_id, self.content, self.com_time.strftime('%Y-%m-%d %H:%M:%S'))
    
class Secret_msg(db.Model):
    __tablename__ = 'secret_msg'

    msg_id = db.Column(INTEGER(unsigned = True), primary_key = True)
    from_user = db.Column(INTEGER(unsigned = True), db.ForeignKey('user.u_id'))
    to_user = db.Column(INTEGER(unsigned = True), db.ForeignKey('user.u_id'))
    msg_content = db.Column(db.Text, nullable = False)
    readed = db.Column(db.Boolean, default = False)
    msg_time = db.Column(db.DateTime, nullable = False)

    def __init__(self, from_user, to_user, msg_content, msg_time):
        self.from_user = from_user
        self.to_user = to_user
        self.msg_content = msg_content
        self.msg_time = datetime.now()

    def __repr__(self):
        return '<Msg(%d, %d, %s, %s)>' % (self.from_user, self.to_user, self.msg_content, \
            self.msg_time.strftime('%Y:%m:%d %H:%M:%S'))

class Group(db.Model):
    __tablename__ = 'group'

    g_id = db.Column(INTEGER(unsigned = True), primary_key = True)
    g_name = db.Column(db.String(50))
    g_hex = db.Column(INTEGER(unsigned = True))

    def __init__(self, g_id, g_name, g_hex):
        self.g_id = g_id
        self.g_name = g_name
        self.g_hex = g_hex

    def __repr__(self):
        return '<Group(%d, %s, %d)>' % (self.g_id, self.g_name, self.g_hex)

class Action(db.Model):
    __tablename__ = 'action'

    act_id = db.Column(INTEGER(unsigned = True), primary_key = True)
    act_name =  db.Column(db.String(50))
    act_hex = db.Column(INTEGER(unsigned = True))

    def __init__(self, act_id, act_name, act_hex):
        self.act_id = act_id
        self.act_name = act_name
        self.act_hex = act_hex

    def __repr__(self):
        return '<Action(%d, %s, %d)>' % (self.act_id, self.act_name, self.act_hex)