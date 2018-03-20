# -*- encoding:utf-8 -*-
import random

from nowstagram import app, db

from flask_script import Manager

from nowstagram.models import User, Image, Comment

manager = Manager(app)
def get_image_url():
    return "https://static.nowcoder.net/head/" + str(random.randint(0,100)) + "m.png"
@manager.command
def init_db():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('user'+str(i+1), 'a'+str(i)))
        for j in range(0,3):
            db.session.add(Image(i+1,get_image_url()))
            for k in range(0,2):
                db.session.add(Comment("comment"+str(i),i+1,  1+3*i+j))
    db.session.commit()
    #print 1, User.query.all()
    #print 2, User.query.get(3)
    #print 3, User.query.filter_by(id=5).first()
    # print 4, User.query.order_by(User.id.desc()).offset(0).limit(2).all()
    # print 5, User.query.filter(User.username.endswith('0')).order_by(User.id.desc()).limit(3).all()
    # print 6, User.query.order_by(User.id.desc()).paginate(page=1, per_page=10).items
    #user = User.query.get(1)
    # print 7, user.images
    image = Image.query.get(1)
    # print 8, image.user
    # comment = Comment.query.get(1)
    # print 9, comment, comment.user

    print 10, image.comment, image.user.username

   # db.session.commit()




if __name__ == '__main__':
    manager.run()