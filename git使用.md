# git使用

### 1、创建本地仓库及使用

```
1、windows下，下载安装GIT.app 按照安装教程
2、打开Git 下Git.Bash  进入黑屏终端
3、在Git.Bash下，进行关联gith配置
   $ git config  --global   user.name   "用户名"
   $ git config  --global   user.email   "邮箱"
4、创建目录，在任意位置创建本地目录文件夹，在Git.Bash下 $cd  将文件夹拖入终端（注：终端为Linux编辑模式）
5、将创建的目录设置为github本地仓库，在创建的目录下直接使用 git init 命令
6、在目录中先创建一文件，cd.txt
7、版本库
   终端下   git add  cd.txt              将文件添加到仓库
           git  commit -m  "注释信息"    将文件提交给仓库
            更改信息，重复提交
8、git status 查看仓库的当前状态，本地仓库任何操作都会报出错误，只有commit 体交完成才不会报错
   git diff   查看修改内容
   git log    查看提交日志，每一次提交所做的不同工作
   git log --pretty  只查看 编号 信息 
 9、版本回退
    git reset --hard  HEAD^       回退到上一次版本
    git reset --hard  HEAD^^      回退到上上次版本
    git reset --hard  HEAD~100    回退到上100次版本
    git reset --hard  具体版号     回退到具体版本 commit  版号不用写全，部分，自动识别
 10、git reflog 记录每一次使用命令
 11、git checkout 撤销
     1、未添加和提交，回退 git checkout -- 文件名，回退到当前提交版本
     2、添加未提交，又修改文件，回退 git checkout -- 文件名，回退到当前添加版本
```

### 2、将本地文件上传到github

```
1、创建SSH Key
   终端下输入 ssh-keygen   -t  rsa  -C  "邮箱"
   一直回车
2、记录 .ssh 目录位置  Created directory '/c/Users/Administrator/.ssh'.
   进入该目录 cd  /c/Users/Administrator/.ssh
   ls 该目录  有两个文件 id_rsa 私钥   id_rsa.pub 公钥
   cat id_rsa.pub  获取秘钥 Ctrl+C Ctrl+V 
 3、登录github
    settings ———— SSH and GPG keys ————粘贴公钥 
 4、测试秘钥是否通过
    $ ssh -T git@github.com 成功就通过
 5、创建远程仓库
     github 下 New repository 创建仓库
 6、关联远程仓库  cd到$ cd /c/Users/Administrator/Desktop/q  本地仓库下
    终端下 git remote add origin 远程仓库地址
    远程仓库地址 在github创建仓库下 Clone or downl 下 Clone with SSH
    复制下面地址
    git remote add origin   删除关联
 7、将本地仓库内容到上传到远程库
    1、先将远程仓库拉到本地仓库，否则报错
       git pull origin master --allow-unrelated-histories
       git pull origin master
    2、将本地仓库内容到上传到远程库
        git push origin master
  8、远程库
     先有远程库
     将远程库 git clone 到本地  Cd到索要创建的目录
     git clone  远程仓库地址
  9、.gitignore文本文件 忽略上传文件，直接将文件名写在.gitignore文本文件下
          
```

3、分支、标签  管理

```
本地管理
1、分支管理   远程下载下来，将目录cd 到下载的仓库下
   分支  合并   
   master 主分支
2、创建分支  git branch  分支名
   切换分支  git checkout 分支名
   创建并切换  git checkout -b 分支名
   git branc  查看所有分支，
              当前所属分支以*开头
3、合并
   切换到主支上
   git merge  分支名  就合并到主支上了
   
远程管理
   在本地分支下
1、将分支远程上传  git push --set-upstream origin ck
   创建远程分支
   以后上传   git push origin   
2、每次重新 git clone 到本地仓库只有master主支，重新创建相同名字的分支，并将    github上的分支内容  git pull origin 拉下来 dev   
3、所有分支工作完成后 ，git add .  git commit -m   
   回到主支下    git branch master
   将分支合并到主支上   git merge  分支名  
   提交到远程仓库   git push origin   dev

```

4、标签管理   版本上线来一标签

```
1、git tag  版本号（本地） V1.0   插入标签
2、git tag  查看标签
3、git checkout  调到标签
4、git show  标签名    查看信息
5、git push origin 标签名  推到远程仓库
6、git push origin --tags  一次性推送
7、删除  先本地  git tag -d 标签名
        在远程   git push origin ： 标签名
        

```

