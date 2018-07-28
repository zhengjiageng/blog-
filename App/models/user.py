from App.extensions import db


class Base:
    #添加一条数据
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
    #添加多条数据
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()
    #自定义删除基类
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()



class User(Base,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    sex = db.Column(db.Boolean,default=True)
    age = db.Column(db.Integer,default=20)
    email = db.Column(db.String(50))
    icon = db.Column(db.String(40),default='default.jpg')
    confirm = db.Column(db.Boolean,default=False) #当前用户是否激活


