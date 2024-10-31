# Generated by Django 5.0.3 on 2024-10-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(default='', max_length=255, verbose_name='文章描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('is_pub', models.BooleanField(default=False, verbose_name='是否发布')),
            ],
        ),
        migrations.CreateModel(
            name='articleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.CharField(max_length=255, verbose_name='评论内容')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='个人博客标题')),
                ('sub_title', models.CharField(default='', max_length=200, verbose_name='个人博客子标题')),
                ('url', models.URLField(verbose_name='个人博客网址')),
                ('theme', models.CharField(max_length=32, verbose_name='博客主题')),
                ('time_zone', models.CharField(default='Eastern China Time (GMT +8)', max_length=32, verbose_name='时区')),
                ('language', models.CharField(default='Chinese - China', max_length=32, verbose_name='语言')),
                ('vip', models.IntegerField(choices=[(0, 'client'), (1, 'Vip'), (2, 'Svip')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='分类标题')),
            ],
        ),
        migrations.CreateModel(
            name='readArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='recommendedArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Subscrible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标签名称')),
            ],
        ),
    ]
