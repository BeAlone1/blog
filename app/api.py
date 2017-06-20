from . import redis_store
from . import db
from .models import *
def get_follow(u_id):
    key = 'follow_' + str(u_id)
    if redis_store.exists(key):
        return redis_store.get(key)
    else:
        q_ret = db.session.query(Follow.follow_id, User.name).filter(Follow.u_id == u_id).filter(Follow.follow_id == User.u_id).all()
        
        for each in q_ret: #如果user在有关注的人的情况下
            redis_store.rpush(key, {"id": each.follow_id, "name": each.name})

        # return redis_store.get(key)
