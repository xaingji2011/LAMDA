from django.db import models

from users.models import User

# Create your models here.
# 博客
class Blog(models.Model):
    """
    博客信息表（站点表）
    """
    vip_choices = (
        (0,'client'),
        (1,'Vip'),
        (2,'Svip')
    )

    title = models.CharField(verbose_name='个人博客标题', max_length=64,unique=True)
    sub_title = models.CharField(verbose_name="个人博客子标题",max_length=200)
    url = models.URLField(verbose_name="个人博客网址",max_length=200)
    theme = models.CharField(verbose_name='博客主题', max_length=32)
    time_zone = models.CharField(verbose_name='时区',max_length=32,default='Eastern China Time (GMT +8)')
    language = models.CharField(verbose_name="语言",max_length=32,default='Chinese - China')
    user = models.OneToOneField(verbose_name="博客作者",to=User,on_delete=models.CASCADE)
    vip = models.IntegerField(choices=vip_choices,default=0)
    
    def __str__(self):
        return self.title
    
    
# 订阅博客
class Subscrible(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="用户")
    blog = models.ForeignKey(verbose_name='所属博客', to=Blog, on_delete=models.CASCADE)
    

# 分类
class Category(models.Model):
    """
    博主个人文章分类表
    """
    title = models.CharField(verbose_name='分类标题', max_length=32)
    blog = models.ForeignKey(verbose_name='所属博客', to=Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

# 标签
class Tag(models.Model):
    title = models.CharField(verbose_name='标签名称', max_length=32)
    blog = models.ForeignKey(verbose_name='所属博客', to=Blog,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

# 文章
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章描述',default='')
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    content = models.TextField(verbose_name="文章内容")
    is_pub = models.BooleanField(verbose_name="是否发布",default=False)
    author = models.ForeignKey(verbose_name='作者', to=User,on_delete=models.CASCADE)  
    category = models.ForeignKey(verbose_name="文章类别",to=Category,null=True,on_delete=models.CASCADE)
    blog = models.ForeignKey(verbose_name='所属博客', to=Blog,on_delete=models.CASCADE)
    tags = models.ManyToManyField(to=Tag)
    
    def __str__(self):
        return self.title
    

# 阅读表
class readArticle(models.Model):
    user = models.ForeignKey(verbose_name='用户',to=User, null=True,on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=True,on_delete=models.CASCADE,verbose_name="文章")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    

class recommendedArticle(models.Model):
    """
    点赞表
    """
    user = models.ForeignKey(verbose_name='用户',to=User, null=True,on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=True,on_delete=models.CASCADE,verbose_name="文章")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    
    
        
class articleComment(models.Model):
    """
    评论表
    """
    user = models.ForeignKey(verbose_name='评论者', to=User,on_delete=models.CASCADE)
    article = models.ForeignKey(verbose_name='评论文章', to=Article,on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    
    parent_comment = models.ForeignKey("self",null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content