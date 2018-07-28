from .main import main
from .test import test
from .user import user

#配置蓝本列表
blueprin_config = [
    (main,''),
    (test,''),
    (user,''),
]


#蓝本的注册
def blueprin_register(app):
    for blue,prefix in blueprin_config:
        app.register_blueprint(blue,url_prefix=prefix)