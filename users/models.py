from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime

# Create your models here.

# 用户
class User(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女')
    )
    

    nick_name = models.CharField('昵称',max_length=50,default='')
    gender = models.CharField('性别',max_length=10,choices=gender_choices,default='male')
    hometown = models.CharField("家乡",max_length=100,default='')
    address = models.CharField("居住地",max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,null=True,blank=True)
    wechat = models.CharField("微信号",max_length=20,null=True,blank=True)
    QQ = models.CharField("QQ号",max_length=20,null=True,blank=True)
    birthday = models.DateField('生日',null=True,blank=True)
    marriage = models.CharField('婚姻',max_length=50,default='')
    position = models.CharField("职位",max_length=50,default='')
    company = models.CharField('公司',max_length=50,default='')
    work_status = models.CharField("工作状况",max_length=20,default='')
    self_introduction = models.CharField("自我介绍",max_length=100,default='')
    avatar = models.ImageField(upload_to='avatars/',default='/avatars/default.png',max_length=100)
    

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.username
    
    
# 验证码模块
class CaptchaModel(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码'),
        ('update_email','修改邮箱')
    )

    code = models.CharField('验证码',max_length=20,default='')
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=30)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
    
    
    
# 关注粉丝表
# class follow(models.Model):
#     # 被关注
#     be_subscribe = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="被关注者",related_name="followers")
#     # 关注
#     subscribe = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="关注者",related_name="followings")
#     # 是否取关
#     is_del = models.BooleanField("是否取关",default=True)
#     # 更新时间
#     update_time = models.DateTimeField("更新时间",auto_now=True)