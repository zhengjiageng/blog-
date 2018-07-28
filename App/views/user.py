from flask import Blueprint,render_template
from App.models import User
from App.forms import Register

user = Blueprint('user',__name__)


@user.route('/register/',methods=['GET','POST'])
def register():
    form=Register()
    if form.validate_on_submit():
       u= User(username=form.username.data,password_hash=form.userpass.data,email=form.email.data)
       u.save()
       return '数据正确'
    return render_template('user/register.html',form=form)