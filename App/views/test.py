from flask import Blueprint,render_template,request,current_app
from App.extensions import db
import random
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize

test = Blueprint('test',__name__)





@test.route('/hashtest/')
def hashTest():
    # password_hash = generate_password_hash('123456')
    # print(password_hash)
    # return 'hash加密{}'.format(password_hash)
    # print(check_password_hash(password_hash,'1234567'))
    s = Seralize(current_app.config['SECRET_KEY'])
    # return 'token{}'.format(s.dumps({'id':1}))
    return '{}'.format(s.loads('eyJpYXQiOjE1MzI0ODU2NjMsImV4cCI6MTUzMjQ4OTI2MywiYWxnIjoiSFMyNTYifQ.eyJpZCI6MX0.tr8vQc0-SlKWnFkoN-iP25PbjvV9yMCFiEl-iVZu8GU')['id'])
    # return '校验hash密码'