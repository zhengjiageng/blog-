from flask import Flask
from .settings import configDict #配置字典
from .extensions import config_extension #第三方扩展库加载
from .views import blueprin_register #注册蓝本

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configDict[configName])
    config_extension(app) #第三方扩展库初始化App
    blueprin_register(app) #注册蓝本

    return app

