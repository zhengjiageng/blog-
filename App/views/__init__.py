from .main import main
from .user import user
from .test import test
#配置蓝本列表  手动添加
blueprin_config = [
    (main,''),
    (user,''),
    (test,''),
]

#蓝本的注册
def blueprin_register(app):
    for blue,prefix in blueprin_config:
        app.register_blueprint(blue,url_prefix=prefix)