from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager #登录处理模块

bootstrap = Bootstrap()
db = SQLAlchemy() #ORM实例化
migrate = Migrate(db=db) #实例化迁移类
mail = Mail()
login_manager = LoginManager()

#初始化所有第三方扩展库
def config_extension(app):
    bootstrap.init_app(app)
    db.init_app(app) #初始化App
    migrate.init_app(app)
    mail.init_app(app)

    login_manager.init_app(app)
    #指定登录端点
    login_manager.login_view = 'user.login'
    #提示信息
    login_manager.login_message = '您还没有登录 请登录在访问'
    #级别有 None，basic strong：会记录客户端的ip和User-agent信息 一旦有异常 自动退出
    login_manager.session_protection = 'strong'



