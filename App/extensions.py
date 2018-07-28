from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy() #ORM实例化
migrate = Migrate(db=db) #实例化迁移类 目的将表单生成传递给数据库，
bootstrap = Bootstrap()

def config_extension(app):
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)


