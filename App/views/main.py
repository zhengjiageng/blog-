from flask import Blueprint

main=Blueprint('main',__name__)


@main.route('/')    #首页路由
def index():
    return 'index'

