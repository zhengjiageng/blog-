from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from App.models import User


#注册表单
class Register(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(message='用户名不能为空'),Length(min=6,max=10,message='用户名为6~10位')],render_kw={'placeholder':'请输入用户名...','maxlength':10})
    userpass = PasswordField('密码',validators=[DataRequired(message='密码不能为空'),Length(min=6,max=16,message='密码长度为6~16位')],render_kw={'placeholder':'请输入密码...','maxlength':16})
    confirm = PasswordField('确认密码',validators=[EqualTo('userpass',message='密码和确认密码不一致')],render_kw={'placeholder':'请输入确认密码...','maxlength':16})
    email = StringField('激活邮箱',validators=[DataRequired(message='邮箱不能为空'),Length(min=6,max=50,message='请输入正确邮箱'),Email(message='请输入正确邮箱')],render_kw={'placeholder':'请输入邮箱...','maxlength':50})
    submit = SubmitField('注册')

    #自定义验证器 验证用户名 和 邮箱是否唯一性
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已存在')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已存在')

# https: // blog.csdn.net / cdnight / article / details / 49636893
#登录表单
class Login(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(message='用户名不能为空'), Length(min=6, max=10, message='用户名为6~10位')],
                           render_kw={'placeholder': '请输入用户名...', 'maxlength': 10})
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=16, message='密码长度为6~16位')],
                             render_kw={'placeholder': '请输入密码...', 'maxlength': 16})
    submit = SubmitField('登录')


class AgainActivate(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(message='用户名不能为空'), Length(min=6, max=10, message='用户名为6~10位')],
                           render_kw={'placeholder': '请输入用户名...', 'maxlength': 10})
    userpass = PasswordField('密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=16, message='密码长度为6~16位')],
                             render_kw={'placeholder': '请输入密码...', 'maxlength': 16})
    submit = SubmitField('激活')

    # 自定义验证器 验证用户名 和 邮箱是否唯一性
    def validate_username(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('激活用户不存在')





