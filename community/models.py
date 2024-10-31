from django.db import models
from users.models import User

# Question

# 问题模型
# class Question(models.Model):
#     author = models.ForeignKey(to=User,verbose_name="问题作者",on_delete=models.CASCADE)
#     title = models.CharField("标题",max_length=64)
#     content = models.TextField("内容")
#     tags = models.CharField("标签",max_length=50)
#     is_draft = models.BooleanField("是否为草稿",default=False)
#     is_recommended = models.IntegerField("是否推荐",default=False)
#     is_solved = models.BooleanField('是否解决',default=False)
#     read_nums = models.IntegerField("浏览量",default=0)
#     reward = models.IntegerField("悬赏积分豆",default=0)
#     create_time = models.DateTimeField("创建时间",auto_now_add=True)
    
#     def __str__(self):
#         return self.title
    
#     def answer_count(self):
#         return self.answer_set.all().count()
    
    
# # 回答模型
# class Answer(models.Model):
#     question = models.ForeignKey(to=Question,verbose_name="问题",on_delete=models.CASCADE)
#     author = models.ForeignKey(to=User,verbose_name="回答作者",on_delete=models.CASCADE)
#     create_time = models.DateTimeField("创建时间",auto_now_add=True)
#     content = models.TextField("内容")
    

# # 用户关注问题
# class followQuestion(models.Model):
#     author = models.ForeignKey(to=User,verbose_name="关注用户",on_delete=models.CASCADE)
#     question = models.ForeignKey(to=Question,verbose_name="问题",on_delete=models.CASCADE)
#     add_time = models.DateTimeField("关注时间",auto_now_add=True)
    

# # 用户点赞回答
# class diggAnswer(models.Model):
#     author = models.ForeignKey(to=User,verbose_name="点赞用户",on_delete=models.CASCADE)
#     answer = models.ForeignKey(to=Answer,verbose_name="回答",on_delete=models.CASCADE)
#     add_time = models.DateTimeField("点赞时间",auto_now_add=True)
 
    
# # 用户收藏回答
# class favoraiteAnswer(models.Model):
#     author = models.ForeignKey(to=User,verbose_name="收藏用户",on_delete=models.CASCADE)
#     answer = models.ForeignKey(to=Answer,verbose_name="回答",on_delete=models.CASCADE)
#     add_time = models.DateTimeField("收藏时间",auto_now_add=True)
    
    
# # 用户评论
# class commentAnswer(models.Model):
#     """
#     评论问题答案
#     """
#     user = models.ForeignKey(verbose_name='评论者',to=User,on_delete=models.CASCADE)
#     answer = models.ForeignKey(to=Answer,verbose_name="回答",on_delete=models.CASCADE)
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#     content = models.CharField(verbose_name='评论内容', max_length=255)
    
#     parent_comment = models.ForeignKey("self",null=True,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.content
    

# # News
# # 新闻分类
# class newsCategory(models.Model):
#     name = models.CharField("新闻分类",max_length=32)
    
#     def __str__(self):
#         return self.name


# # 新闻
# class News(models.Model):
#     category = models.ForeignKey(to=newsCategory,on_delete=models.CASCADE)
#     title = models.CharField("标题",max_length=32)
#     content = models.TextField("内容")
#     pub_time = models.DateTimeField("发布时间",auto_now_add=True)
#     author = models.ForeignKey(verbose_name="投递人",to=User,on_delete=models.CASCADE)
#     read_nums = models.IntegerField("浏览量",default=0)
#     is_recommended = models.BooleanField("是否推荐",default=False)
    
    
# # 用户收藏新闻
# class favoraiteNews(models.Model):
#     author = models.ForeignKey(to=User,verbose_name="用户",on_delete=models.CASCADE)
#     news = models.ForeignKey(to=News,verbose_name="新闻",on_delete=models.CASCADE)
#     add_time = models.DateTimeField("收藏时间",auto_now_add=True)


# # 阅读表
# class readNews(models.Model):
#     user = models.ForeignKey(verbose_name='用户',to=User, null=True,on_delete=models.CASCADE)
#     article = models.ForeignKey(News, null=True,on_delete=models.CASCADE,verbose_name="新闻")
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    

# class recommendedNews(models.Model):
#     """
#     推荐表
#     """
#     user = models.ForeignKey(verbose_name='用户',to=User, null=True,on_delete=models.CASCADE)
#     article = models.ForeignKey(News, null=True,on_delete=models.CASCADE,verbose_name="文章")
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    
# # 用户评论
# class commentnews(models.Model):
#     """
#     评论新闻
#     """
#     user = models.ForeignKey(verbose_name='评论者',to=User,on_delete=models.CASCADE)
#     news = models.ForeignKey(to=News,verbose_name="新闻",on_delete=models.CASCADE)
#     create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#     content = models.CharField(verbose_name='评论内容', max_length=255)
    
#     parent_comment = models.ForeignKey("self",null=True,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.content
    

# # 小组Group
# # 小组分类
# class groupCategory(models.Model):
#     name = models.CharField("分类名称",max_length=20)


# # 小组表
# class Group(models.Model):
#     category = models.ForeignKey(groupCategory,on_delete=models.CASCADE)
#     title = models.CharField("标题",max_length=20)
#     type = models.CharField("小组类型",max_length=20)
#     tags = models.CharField("小组标签",max_length=50)
#     introduction = models.CharField("小组介绍",max_length=200)
#     notice = models.CharField("小组公告",max_length=200)
#     avatar = models.ImageField(upload_to="group/avatars",default="group/avatars/default.png",max_length=200)
#     create_time = models.DateTimeField("创建时间",auto_now_add=True)
    
#     def __str__(self):
#         return self.title
    
    
# # 小组成员表
# class groupMember(models.Model):
#     LEVEL_CHOICES = (
#         ('leader',"组长"),
#         ('assistant',"组长助理"),
#         ('senior_member',"高级组员"),
#         ('member',"组员")
#     )
    
#     group = models.ForeignKey(to=Group,on_delete=models.CASCADE,verbose_name="小组")
#     user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="小组成员")
#     level = models.CharField("用户级别",choices=LEVEL_CHOICES)
#     create_time = models.DateTimeField("进入房间时间",auto_now_add=True)
    

# # 聊天记录
# class chatMessage(models.Model):
#     # MSG_CHOICES = (
#     #     ('user',"用户消息"),
#     #     ('system',"系统消息"),
#     # )
    
#     MSG_CHOICES = (
#         ('text',"文本"),
#         ('voice',"语音"),
#         ('redEnvelope',"红包"),
#         ('img',"图片"),
#         ('goods',"商品链接")
#     )
    
#     STATUS_CHOICES = (
#         ('0',"未读消息"),
#         ('1',"已读消息"),
#         ('2',"消息已撤回")
#     )
    
#     # type = models.CharField("消息类型",choices=MSG_CHOICES)
#     sender = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="发送者")
#     reciever = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="接受者")
#     group = models.ForeignKey(to=Group,on_delete=models.CASCADE,verbose_name="小组") 
#     content = models.CharField("聊天内容",max_length=200)
#     send_time = models.DateTimeField("创建时间",auto_now_add=True)
#     msg_type = models.CharField("消息类型",choices=MSG_CHOICES)
#     status = models.CharField("消息状态",choices=STATUS_CHOICES)

    
# # 黑名单
# class blackList(models.Model):
#    user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="用户") 
#    blacklist = models.TextField("黑用户名单")
   
   
   
# # 会员
# class OrderInfo(models.Model):
#     PAY_METHOD_CHOICES = (
#         (1, "支付宝"),
#         (2, "微信"),
#     )

    
#     order_id = models.CharField(max_length=64,primary_key=True,verbose_name="订单编号")
#     user = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="下单用户")
    
#     total_account = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="支付总金额")
#     pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES,default=1,verbose_name="支付方式")
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    
# class Payment(models.Model):
#     order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE,verbose_name="订单")
#     trade_id = models.CharField(max_length=100,unique=True,null=True,blank=True,verbose_name="支付编号")
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
#     class Meta:
#         db_table = 'tb_payment'
#         verbose_name = '支付信息'
#         verbose_name_plural = verbose_name