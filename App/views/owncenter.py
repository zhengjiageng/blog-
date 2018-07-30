from flask import Blueprint,render_template,current_app
from App.forms import UploadPhotos
from App.extensions import file
import os,string,random
from PIL import Image
from flask_login import current_user,login_required
from App.extensions import db
center = Blueprint('center',__name__)

#生成随机的名字
def random_name(suffix,length=32):
    Str = string.ascii_letters+string.digits
    return ''.join(random.choice(Str) for i in range(length))+'.'+suffix

#图片缩放函数
def img_zoom(path,width=200,height=200,prefix='s_'):
    img = Image.open(path)
    print(img.size)  # 获取图片的宽 高
    img.thumbnail((width, height))  # 重新设计尺寸
    pathSplit = os.path.split(path) # 将路径拆分成 路径和文件名
    newPath = os.path.join(pathSplit[0],prefix+pathSplit[1]) #将前缀进行拼接
    img.save(newPath)  # 保存图片 覆盖掉原来的图片

#文件上传
@center.route('/upload/',methods=['GET','POST'])
@login_required
def upload():
    img_url = file.url('default.jpg') #获取默认头像的地址
    form = UploadPhotos() #表单类实例化
    if form.validate_on_submit():
        photo = form.photo.data #获取上传的文件
        suffix = photo.filename.split('.')[-1] #获取后缀
        #在这个基础上完善  upload下存放图片 以每个人的username为名 存储当前用户的所有图片
        #生成唯一的随机图片名
        while True:
            newName = random_name(suffix)
            path = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],newName)
            if not os.path.exists(path):
                break
        #保存上传图片
        file.save(photo,name=newName)
        #删除之前上传的图片
        if current_user.icon != 'default.jpg':
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon))
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],'s_'+current_user.icon))
        img_zoom(path) #进行缩放
        current_user.icon = newName
        db.session.add(current_user) #把修改后的图片名 保存到表中
        db.session.commit()
        img_url = file.url(current_user.icon) #获取上传后的图片地址
    return render_template('owncenter/photo.html',form=form,img_url=img_url)