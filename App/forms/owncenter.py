from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import SubmitField
from App.extensions import file

class UploadPhotos(FlaskForm):
    photo = FileField('上传头像',validators=[FileRequired(message='您还没有选择文件'),FileAllowed(file,message='请选择正确格式的图片')])
    submit = SubmitField('上传')


