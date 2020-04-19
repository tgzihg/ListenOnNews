# 学习Github和Git命令
[toc]
## 事前：VSCode插件推荐安装
gitlens和git history
## 入门
1. 仓库初始化：VSCode中打开项目文件夹，打开终端，输入下述命令初始化本项目文件夹，将目录初始化为一个仓库
```
git init
```
2. 添加缓冲区：项目文件夹中创建一个文件（如demo.py)，修改并保存文件，之后输入下述命令将文件从**工作区**添加到**缓冲区**。缓冲区的作用是：你可以多次add文件到缓冲区。
```
git add .\demo.py
```
3. 添加到归档区：然后输入下述命令将文件从缓冲区到**归档区**。-m添加注释
```
git commit -m "添加了文件XXX"
```
4. 添加远端仓库：下述命令添加了一个远端的仓库，使用https。注意，在此之前应确定该仓库存在~，需要自己在github上创建好仓库~
- remote：添加远程仓库
- origin：远程仓库的名字
- https://...//RepoName：远程仓库链接
```
git remote add origin https://github.com/XXX/YYY.git
```
5. 归档区提交到远端仓库：将归档区的内容全部添加到远端仓库，实现从归档区上传到远程仓库：XXX/YYY.git。
- origin: 远端仓库
- master: 提交到这个仓库的master分支
```
git push -u origin master
```
### 注意：
- 三个区：工作区->缓冲区->归档区--*remote*-->远程仓库
- 归档区一定要有的，本地的代码归档是非常必要的，远端仓库其实并不重要。
- 缓冲区的必要性：如果连续多次将本地文件添加到缓冲区，即多次执行*add*，然后可以执行一次commit，将所有内容添加到归档区。
## 其它
查看当前本地git仓库状态：
```
git status
```
红色的内容说明还没有/修改后添加到缓冲区。
绿色的说明已经添加到缓冲区*但是还没有添加到归档区*
使用
```
git add .
```
可以将当前目录下所有内容添加到缓冲区。

使用
```
git commit -m "XXX"
```
将所有改动一次提交到本地归档区

使用
```
git push origin master
```
将本地归档区上传到远端仓库。

## 代码的回滚
通过git插件，上方的*Git:View History*打开Git历史图形界面，可以看到该项目的一些版本。

通过*混合回滚*命令可以将项目的*归档区和缓冲区*回滚到HASHCODE对应的提交版本中。
```
git reset --mixed *HASHCODE*
```
查看操作的记录，可以查看对应之前版本的hash码：
```
git reflog
```
硬回滚，将*归档区、缓冲区、工作区*全部进行回滚：
```
git reset --hard *HASHCODE*
```
软回滚，只将归档区进行了回滚，但是工作区和缓冲区不操作：
```
git reset --soft *HASHCODE*
```
