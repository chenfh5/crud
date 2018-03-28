A CRUD Framework
================
[![Build status](https://ci.appveyor.com/api/projects/status/y02knj78is0syqh6?svg=true)](https://ci.appveyor.com/project/chenfh5/crud)

> A [create, read, update, and delete](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) framework base on [Django](https://github.com/django/django)

# Environment
- [Python 3.6.4](https://www.python.org/downloads/release/python-364/) or [Anaconda3-5.1.0](https://www.anaconda.com/download/)
- [Django 2.0.3](https://www.djangoproject.com/download/)

# Reference
- [Django Getting started](https://docs.djangoproject.com/en/2.0/intro/)
- [Python3 教程 From Runoob](http://www.runoob.com/python3/python3-tutorial.html)
- [Python3 教程 From Liaoxuefeng](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
- [Django 教程](www.runoob.com/django/django-tutorial.html)


# Steps
1. cd `dir` & run `django-admin startproject mysite` 自动生成mysite项目
2. run `python manage.py runserver 9000` 启动一个server
3. run `python manage.py makemigrations polls` 将模型文件的变化固话为migration
4. run `python manage.py sqlmigrate polls 0001` migration的具体sql语句描述
5. run `python manage.py migrate ` 执行sql语句
6. `http://127.0.0.1:9000/admin/polls/question/` 填写问题的`题目`和`时间`

![Django tutorial02 snapshot](https://upload-images.jianshu.io/upload_images/2189341-e3810eb6effaaab3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
