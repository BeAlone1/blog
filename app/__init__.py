from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_cache import Cache
from flask_redis import FlaskRedis

db = SQLAlchemy()
sess = Session()
cache = Cache()
redis_store = FlaskRedis()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py', silent = False)
    db.init_app(app)
    sess.init_app(app)
    cache.init_app(app)
    redis_store.init_app(app)

    from .main import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app
