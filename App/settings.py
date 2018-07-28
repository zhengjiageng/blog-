#打开数据库  net start mysql57
            # mysql -u root -p
class Config:
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    BOOTSTRAP_SERVE_LOCAL = True

#开发环境
class DevelopmentConfig(Config):               #用户名 密码   ip       端口号  数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:caijing123@127.0.0.1:3306/python1807'
    DEBUG = True  #开启调试模式

#测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:caijing123@127.0.0.1:3306/python1807'
    DEBUG = False

#生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blog'
    DEBUG = False

#配置的字典
configDict = {
    'default':DevelopmentConfig,
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig
}