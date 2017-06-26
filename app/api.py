from . import redis_store
from . import db
from .models import *
def get_follow(u_id):
    key = 'follow_' + str(u_id)
    if redis_store.exists(key):
        return redis_store.lrange(key, 0, redis_store.llen(key) - 1)
        
    else:
        q_ret = db.session.query(Follow.follow_id, User.name).filter(Follow.u_id == u_id).filter(Follow.follow_id == User.u_id).all()
        
        if len(q_ret) == 0:
            return None
        for each in q_ret: #如果user在有关注的人的情况下
            redis_store.rpush(key, {"u_id": each.follow_id, "name": each.name})

        return redis_store.lrange(key, 0, redis_store.llen(key) - 1)

def get_blog(art_id):
    key = 'article_' + str(art_id)

    if redis_store.exists(key):
        return redis_store.hkeys(key)