from App.extensions import db
from werkzeug.security import generate_password_hash,check_password_hash
#生成token值  加密令牌  确定是谁访问的我（是否是自己人来访问）
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize
from flask import current_app
from App.extensions import login_manager
from flask_login import UserMixin

class Base:
    #添加一条数据
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
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


class User(UserMixin,Base,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    sex = db.Column(db.Boolean,default=True)
    age = db.Column(db.Integer,default=20)
    email = db.Column(db.String(50))
    icon = db.Column(db.String(40),default='default.jpg')
    confirm = db.Column(db.Boolean,default=False) #当前用户是否激活
    """
    参数1  引用关系的模型
    参数2  backref  反向引用的字段  给posts模型 添加了一个user属性 这个属性是替代uid 来进行对象的查询的 uid这个字段用不上
    参数3  加载数据条目（如何加载）
        dynamic  返回query对象  也就是你所看到的sql语句
        默认是select....  返回 一个列表 装有所有帖子对象的列表
            不用的原因：不能呢个通过过滤器 再次筛选或者其它操作
    """
    # posts = db.relationship('Posts',backref='user',lazy='dynamic')
    posts = db.relationship('Posts',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('密码不可读')
    #将明文密码 变成hash加密在赋给 字段属性 password_hash
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    #验证用户密码
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    # 生成token    通过邮件发送token值 进行账户的激活
    def generate_token(self):
        s = Seralize(current_app.config['SECRET_KEY'])
        return s.dumps({'id': self.id})

    #检测token值是否正确
    @staticmethod
    def check_token(token):
        s = Seralize(current_app.config['SECRET_KEY'])
        try:
            Dict = s.loads(token) #加载出token的字典
            id = Dict['id'] #拿到用户的id
            u = User.query.get(id) #查询id的对象是否存在 在则为 <user n> 否则为None
            if not u:
                raise ValueError
            #以上的代码只有出现问题 则都执行except
        except:
            return False
        #判断账户是否没有激活  没有则激活 激活了则返回True
        if not u.confirm:
            u.confirm = True
            u.save()

        return True


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)