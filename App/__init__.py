
from .views import blueprin_register
from .extensions import config_extension

from  flask import  Flask
from .settings import configDict
from .extensions import config_extension
from .views import blueprin_register


def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configDict[configName])
    config_extension(app) #第三方库初始化app
    blueprin_register(app)#注册蓝本

    return app
#   将 aPP  单独写入

