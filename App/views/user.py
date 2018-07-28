from flask import Blueprint,render_template,flash,redirect,url_for
from App.models import User
from App.forms import Register,Login,AgainActivate
from App.email import send_mail
from flask_login import login_user,logout_user,login_required,current_user

user = Blueprint('user',__name__)



"""
1.判断用户名 邮箱是否唯一
2.实例化User类  并将密码加密
3.u.save()
4.配置发送邮件 token
5.发送邮件 携带
6.告诉用户 注册成功  前去邮箱进行激活
7.写一个邮箱激活的视图函数
8.激活之后 告诉激活成功  前去登录
"""



@user.route('/register/',methods=['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        u = User(username=form.username.data,password=form.userpass.data,email=form.email.data)
        u.save()
        token = u.generate_token() #获取token值
        send_mail('账户激活',u.email,username=u.username,token=token)
        flash('账户注册成功！请前往邮箱中进行账户的激活')
        return redirect(url_for('user.login'))
    return render_template('user/register.html',form=form)


#激活账户
@user.route('/activate/<token>/')
def activate(token):
    #调用校验token的方法  激活成功或者失败
    if User.check_token(token):
        flash('激活成功！请登录')
        return redirect(url_for('user.login'))
    else:
        flash('激活失败 请重新点击激活码 进行账户的激活')
        return redirect(url_for('user.register'))


#激活链接地址失效 再次激活
@user.route('/again_activate/',methods=['GET','POST'])
def again_activate():
    form = AgainActivate()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash('激活用户不存在')
        elif u.confirm:
            flash('该用户已经激活 请前去登录')
        elif not u.check_password(form.userpass.data):
            flash('密码不正确')
        else:
            token = u.generate_token()
            send_mail('邮箱激活',u.email,username=u.username,token=token)
            flash('激活邮件已发送 请前去邮箱中激活')
    return render_template('user/again_activate.html',form=form)






#登录
@user.route('/login/',methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        print(u)
        if not u:
            flash('当前用户不存在')
        elif not u.confirm:
            flash('您还没有进行账户的激活')
        elif u.check_password(form.userpass.data):
            flash('登录成功！欢迎'+u.username)
            login_user(u)
            return redirect(url_for('main.index')) #重定向到首页
        else:
            flash('请输入正确的密码')
    return render_template('user/login.html',form=form)

#退出登录
@user.route('/logout/')
def logout():
    logout_user()
    return '退出成功'

#必须登录才能访问的路由地址
@user.route('/center/')
@login_required
def center():
    return '必须登录才能访问'

#实现  登录的时候  有next 参数 则重定向到next路由地址  否则去首页