# -*- endcoding=UTF-8 -*-
import random

from nowstagram import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1024))
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'),)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),)
    statues = db.Column(db.Integer, default=0) #0 正常 1 删除
   # user = db.relationship('User', backref='Comment')
    user = db.relationship('User')
    def __init__(self, content, user_id, image_id):
        self.content = content
        self.user_id = user_id
        self.image_id = image_id

    def __repr__(self):
        return "<Content %d, %s>" % (self.id, self.content)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),)
    url = db.Column(db.String(256))
    create_time = db.Column(db.DateTime)
    comment = db.relationship('Comment')

    def __init__(self, user_id, url):
        self.user_id = user_id
        self.url = url
        self.create_time = datetime.now()
    def __repr__(self):
        return "<Image %d, %s>" % (self.id, self.url)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    images = db.relationship('Image', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.head_url = "https://static.nowcoder.net/head/" + str(random.randint(0,100)) + "m.png"

    def __repr__(self):
        return "<Userid: %d, Username:%s>" % (self.id, self.username)