from .main import main #首页蓝本
from .test import test  #测试使用蓝本
from .user import user  #用户登录 注册 激活的蓝本
from .owncenter import center  #个人中心的蓝本
from .posts import posts  #帖子的蓝本
#配置蓝本列表
blueprin_config = [
    (main,''),
    (test,''),
    (user,''),
    (center,''),
    (posts,''),
]


#蓝本的注册
def blueprin_register(app):
    for blue,prefix in blueprin_config:
        app.register_blueprint(blue,url_prefix=prefix)