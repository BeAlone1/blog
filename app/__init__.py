from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
db = SQLAlchemy()
sess = Session()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py', silent = False)
    db.init_app(app)
    sess.init_app(app)

    return app

if __name__ == "__main__":
    create_app().run('0.0.0.0', 8899)
