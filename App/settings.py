import os

class Config:
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True #设置自动提交
    BOOTSTRAP_SERVE_LOCAL = True

    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.qq.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','793096086@qq.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','zqxvwjfqykgobbjf')



#开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:caijing123@127.0.0.1:3306/python1807'
    DEBUG = True


#测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test_blog'
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