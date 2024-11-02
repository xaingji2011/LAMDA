from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.http import JsonResponse

from users.models import User
from blog.models import Article,Blog,Category,Tag
from .forms import ArticleForm,TagForm
from utils.mixin_utils import LoginRequiredMixin

import math
# Create your views here.


# 个人博客首页
class blogIndexView(LoginRequiredMixin,View):
    def get(self,request,title):
        #当前页面
        current_page = request.GET.get('page',1)
        current_page = int(current_page)
        # 博客对象
        try:
            blog_obj = Blog.objects.get(title=title)
        except Exception as e:
            return render(request,'404.html',{})

        # 当前用户下所有文章列表
        article_list = Article.objects.filter(blog=blog_obj)
        
        # 添加分页功能
        paginatorObj = Paginator(object_list=article_list,per_page=8)
        # 当前页
        page_article_obj = paginatorObj.page(current_page)
        
        # 添加页码数
        start = current_page - math.ceil(10/2)
        
        if start < 1:
            start = 1
        end = start + 9
        
        if end > paginatorObj.num_pages:
            end = paginatorObj.num_pages
        
        if end < 10:
            start = 1
        else:
            start = end - 9
            
        page_list = range(start,end+1)

        
        return render(request,'blog/index.html',{
            'articleList':page_article_obj,
            'pageList':page_list,
            })
        

# 个人博客发布文章
# class blogPubView(LoginRequiredMixin,View):
#     def get(self,request):
#         # 博客对象
#         try:
#             blog_obj = Blog.objects.get(user=request.user)
#         except Exception as e:
#             return render(request,'404.html',{})
        
#         category_list = Category.objects.filter(blog=blog_obj)
#         tag_list = Tag.objects.filter(blog=blog_obj)
        
#         return render(request,'blog/pub_blog.html',{'categories':category_list,'tags':tag_list})
    
#     def post(self,request):
#         form = PubBlogForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             category_id = form.cleaned_data.get('category')
#             article = Article.objects.create(title=title, content=content, category_id=category_id,author=request.user)
#             tags = form.cleaned_data.get('tags')
#             tagIDList = tags.split(";")
#             for tagID in tagIDList:
#                 tag_obj = Tag.objects.get(id=int(tagID))
#                 article.tags.add(tag_obj)
            
#             return render(request,'blog/article.html',{})
#         else:
#             print(form.errors)
#             return JsonResponse({'code': 400, "message": "参数错误！"})


# # 分类页
# class homeCategoryView(View):
#     def get(self,request,username,**kwargs):
#         #当前页面
#         current_page = request.GET.get('page')
#         # 当前类别
#         category = kwargs.get('category')
#         # 用户对象
#         user_obj = User.objects.filter(username=username).exists()
#         # 判断用户是否存在
#         if not user_obj:
#             return JsonResponse({'code':400,'msg':"not found"})
#         # 当前用户下所有文章列表
#         article_list = Article.objects.filter(user=user_obj).filter(category__title=category)
        
#         # 添加分页功能
#         paginatorObj = Paginator(object_list=article_list,per_page=8)
#         # 当前页
#         page_article_obj = paginatorObj.page(current_page)
        
#         # 添加页码数
#         start = current_page - math.ceil(10/2)
        
#         if start < 1:
#             start = 1
#         end = start + 9
        
#         if end > paginatorObj.num_pages:
#             end = paginatorObj.num_pages
        
#         if end < 10:
#             start = 1
#         else:
#             start = end - 9
            
#         page_list = range(start,end+1)
   
        
#         return render(request,'blog/home_site.html',{
#             'articleList':page_article_obj,
#             'pageList':page_list,
#             })
        

# # 标签页
# class homeTagView(View):
#     def get(self,request,username,**kwargs):
#         #当前页面
#         current_page = request.GET.get('page')
#         # 当前标签
#         tag = kwargs.get('tag')
#         # 用户对象
#         user_obj = User.objects.filter(username=username).exists()
#         # 判断用户是否存在
#         if not user_obj:
#             return JsonResponse({'code':400,'msg':"not found"})
#         # 当前用户下所有文章列表
#         article_list = Article.objects.filter(user=user_obj).filter(tags__title=tag)
        
#         # 添加分页功能
#         paginatorObj = Paginator(object_list=article_list,per_page=8)
#         # 当前页
#         page_article_obj = paginatorObj.page(current_page)
        
#         # 添加页码数
#         start = current_page - math.ceil(10/2)
        
#         if start < 1:
#             start = 1
#         end = start + 9
        
#         if end > paginatorObj.num_pages:
#             end = paginatorObj.num_pages
        
#         if end < 10:
#             start = 1
#         else:
#             start = end - 9
            
#         page_list = range(start,end+1)
   
        
#         return render(request,'blog/home_site.html',{
#             'articleList':page_article_obj,
#             'pageList':page_list,
#             })


# # 归档
# class homeArchiveView(View):
#     def get(self,request,**kwargs):
#         current_page = request.GET.get('page')
#         if kwargs:
#             username = kwargs.get('username')
#             year = kwargs.get('year')
#             month = kwargs.get('month')
#         user_obj = User.objects.filter(username=username).exists()
#         # 判断用户是否存在
#         if not user_obj:
#             return JsonResponse({'code':400,'msg':"not found"})
#         # 当年当月的文章列表
#         article_list = Article.objects.filter(user=user_obj).filter(create_time__year=year,create_time__month=month)
        
#         # 添加分页功能
#         paginatorObj = Paginator(object_list=article_list,per_page=8)
#         # 当前页
#         page_article_obj = paginatorObj.page(current_page)
        
#         # 添加页码数
#         start = current_page - math.ceil(10/2)
        
#         if start < 1:
#             start = 1
#         end = start + 9
        
#         if end > paginatorObj.num_pages:
#             end = paginatorObj.num_pages
        
#         if end < 10:
#             start = 1
#         else:
#             start = end - 9
            
#         page_list = range(start,end+1)
        
#         return render(request,'blog/home_site.html',{
#             'articleList':page_article_obj,
#             'pageList':page_list,
#             })

        

# # 点赞
# class diggView(View):
#     def get(self,request):
#         article_id = request.POST.get("article_id")
#         is_up = json.loads(request.POST.get("is_up"))
#         user_id = request.user.pk
        
#         response = {"state":True, "msg":None, "handled":None}
        
#         obj = ArticleUpDown.objects.filter(user_id=user_id,article_id=article_id).first()
        
#         if not obj:
#             # 创建一条点赞记录
#             ard = ArticleUpDown.objects.filter(user_id=user_id,is_up=is_up,article_id=article_id)
#             # 点赞数的保存
#             queryset = Article.objects.filter(pk=article_id)
#             if is_up:
#                 queryset.update(up_count=F('up_count')+1)
#             else:
#                 queryset.update(down_count=F('down_count')-1)
#         else:
#             response['state'] = False
#             response['handled'] = obj.is_up
        
#         return JsonResponse(response)
            
            
        
# # 评论
# class commentView(View):
#     def post(self,request):
#         article_id = request.POST.get("article_id")
#         content = request.POST.get("content")
#         parent_id = request.POST.get("parent_id")
#         user_id = request.user.pk
        
#         comment_obj = Comment.objects.create(user_id=user_id,article_id=article_id,content=content,parent_comment_id=parent_id)
        
#         response = {}
#         response["create_time"] = comment_obj.create_time.strftime("%Y-%m-%d %X")
#         response["username"] = request.user.username
#         response["content"] = content
        
#         return JsonResponse(response)
        
        
# # 文章详情页
# class articleDetailView(View):
#     def get(self,request,username,article_id):
#         user_obj = User.objects.filter(username=username).first()
#         blog = user_obj.blog
        
#         # article_id对应的文章
#         article_obj = Article.objects.filter(pk=article_id).first()
        
#         # 评论显示
#         comment_list = Comment.objects.filter(article_id=article_id).all()
        
#         return render(request,'blog/article_detail.html',{'commentList':comment_list})

# # 聊天 
# class chatView(View):
#     def get(self,request):
#         return render(request,'chat.html',{})
    

# # 留言
# class messageView(View):
#     def get(self,request,username,**kwargs):
#         #当前页面
#         current_page = request.GET.get('page')
#         # 用户对象
#         user_obj = User.objects.filter(username=username).exists()
#         # 判断用户是否存在
#         if not user_obj:
#             return JsonResponse({'code':400,'msg':"not found"})
#         # 当前博客下的所有留言
#         message_list = Message.objects.filter(user=user_obj)
        
#         # 添加分页功能
#         paginatorObj = Paginator(object_list=message_list,per_page=8)
#         # 当前页
#         page_article_obj = paginatorObj.page(current_page)
        
#         # 添加页码数
#         start = current_page - math.ceil(10/2)
        
#         if start < 1:
#             start = 1
#         end = start + 9
        
#         if end > paginatorObj.num_pages:
#             end = paginatorObj.num_pages
        
#         if end < 10:
#             start = 1
#         else:
#             start = end - 9
            
#         page_list = range(start,end+1)
   
        
#         return render(request,'blog/home_site.html',{
#             'articleList':page_article_obj,
#             'pageList':page_list,
#             })


#     def post(self,request):
#         form = messageForm(request.POST)
#         if form.is_valid():
#             blog_id = form.cleaned_data.get('blog')
#             content = form.cleaned_data.get('content')
#             Message.objects.create(user=request.user,blog_id=blog_id,content=content)
#             return redirect('/blog/message')
#         else:
#             return JsonResponse
        
        
# # docassemble模块   
# class docassembleView(View):
#     def get(self,request):
#         return render(request,'docassemble.html')