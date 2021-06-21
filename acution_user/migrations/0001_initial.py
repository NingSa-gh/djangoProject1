# Generated by Django 3.2.4 on 2021-06-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acution_users',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='用户id')),
                ('name', models.CharField(max_length=20, verbose_name='用户名字')),
                ('phone', models.CharField(max_length=11, verbose_name='用户手机号')),
                ('info', models.CharField(max_length=100, verbose_name='用户简介')),
                ('password', models.CharField(max_length=16, verbose_name='用户登录密码')),
                ('address', models.CharField(max_length=140, verbose_name='用户收货地址')),
                ('create_time', models.CharField(max_length=40, verbose_name='用户创建时间')),
                ('user_image', models.ImageField(default='ic_defultuserface.png', upload_to='userface')),
                ('balance', models.FloatField(max_length=10, verbose_name='用户余额')),
            ],
        ),
    ]
