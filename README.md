A CRUD Framework
================
[![Build status](https://ci.appveyor.com/api/projects/status/y02knj78is0syqh6?svg=true)](https://ci.appveyor.com/project/chenfh5/crud)

> A [create, read, update, and delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) framework base on [Django](https://github.com/django/django)

# Environment
- [Python 3.6.4](https://www.python.org/downloads/release/python-364/) or [Anaconda3-5.1.0](https://www.anaconda.com/download/)
- [Django 2.0.3](https://www.djangoproject.com/download/)

# Reference
- [Django Getting started](https://docs.djangoproject.com/en/2.0/intro/)
- [Full CRUD with Django 2.0 in 30 minutes ( 2018 )](https://www.youtube.com/watch?v=Kf9KB_TZY5U)
- [Python3 教程 From Runoob](http://www.runoob.com/python3/python3-tutorial.html)
- [Python3 教程 From Liaoxuefeng](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
- [Django 教程](www.runoob.com/django/django-tutorial.html)


# Steps
1. cd `classpath` & run `django-admin startproject bookShop` 自动生成mysite项目
2. cd `classpath/bookShop` & run `python manage.py startapp books` 创建app来使用模型model模块
3. run `python manage.py makemigrations` 将模型文件的变化固话为migration
4. run `python manage.py sqlmigrate books 0001` migration的具体sql语句描述
5. run `python manage.py migrate` 执行sql语句
6. run `python manage.py createsuperuser` 建用户
7. run `python manage.py runserver` 启动一个server

![Django tutorial02 snapshot](https://upload-images.jianshu.io/upload_images/2189341-e3810eb6effaaab3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![list_books](https://upload-images.jianshu.io/upload_images/2189341-c8d72571becd39cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![create/update a book](https://upload-images.jianshu.io/upload_images/2189341-f38003794e47c742.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![delete a book](https://upload-images.jianshu.io/upload_images/2189341-124346ecd2d9d9c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![admin](https://upload-images.jianshu.io/upload_images/2189341-a516b9745be820f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
