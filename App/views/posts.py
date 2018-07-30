from flask import Blueprint,render_template
from App.forms import SendPosts
from App.models import Posts
from flask_login import current_user

posts = Blueprint('posts',__name__)

#发表帖子
@posts.route('/send_posts/',methods=['GET','POST'])
def send_posts():
    form = SendPosts()
    if form.validate_on_submit():
        print(form.article.data)
        p = Posts(title=form.articletitle.data,article=form.article.data,user=current_user)
        p.save()
    return render_template('posts/send_posts.html',form=form)


@posts.route('/show/')
def show():
    from App.models import User
    # p = Posts.query.get(1)
    # print(p)
    # print(p.user.username)
    # print(p.uid)
    # u = User.query.get(1)
    # print(u.posts)
    # print(u.posts.all())
    # print(u.posts.filter())
    # print(u.posts.filter_by(id=1).first())
    return '测试'