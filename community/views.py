from django.shortcuts import render,redirect
from django.views import View
from django.http.response import JsonResponse
from django.core.paginator import Paginator
# from django.utils.timezone import now
# from django.db.models import Count

# from .models import Question,Answer,commentAnswer,readNews
# from blog.models import Article,readArticle,recommendedArticle,articleComment
from blog.models import Article
from blog.models import Blog
from .forms import blogRegisterForm
# from .forms import QuestionForm,AnswerForm,commentForm,addEditArticleForm
# from users.models import User

import math
from datetime import timedelta
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.
# LAMDA社区首页
class IndexView(View):
    def get(self,request):
        current_page = request.GET.get('page',1)
        article_list = Article.objects.all().order_by('-create_time')

        try: 
            title = Blog.objects.get(user=request.user).title
        except Exception as e:
            return render(request,'404.html',{})

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
        
        return render(request,'index.html',{'article_list':page_article_obj,'page_list':page_list,'title':title})



# 博客注册
class blogRegisterView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'blog_register.html',{})
    
    def post(self,request):
        form = blogRegisterForm(request.POST)	
        if form.is_valid():
            sub_url = form.cleaned_data.get('sub_url')
            url = 'http://127.0.0.1:8000/blog/' + sub_url
            theme = form.cleaned_data.get('theme')
            blog_obj = Blog.objects.create(title=sub_url,url=url,theme=theme,user=request.user)
            return render(request,'blog_register_success.html',{'url':url}) 
        else:
            return JsonResponse({'code':400,'message':'参数错误!'})
        

class profileIndexView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'profile.html',{})

# # 咨询问题
# class askQuestionView(View):
#     def post(self,request):
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             author_id = form.cleaned_data.get('author')
#             content = form.cleaned_data.get('content')
#             title = form.cleaned_data.get('title')
#             tags = form.cleaned_data.get('tags')
#             is_draft = form.cleaned_data.get('is_draft')
#             reward = form.cleaned_data.get('reward')

#             Question.objects.create(
#                 title = title,
#                 content = content,
#                 tags = tags,
#                 is_draft = is_draft,
#                 reward = reward,
#                 author_id = author_id
#             )
            
#             return render(request,'question/new.html',{})
#         else:
#             return JsonResponse({"code":400,"msg":"参数错误!"})
    
# # 问题首页
# class questionIndexView(View):
#     def get(self,request):
#         # 默认未解决
#         question_list = Question.objects.filter(is_solved=False).order_by('-create_time')
#         return render(request,'question/index.html',{'question_list':question_list})
    

# # 已解决的问题页
# class questionSolvedView(View):
#     def get(self,request):
#         question_list = Question.objects.filter(is_solved=True).order_by('-create_time')
#         return render(request,'question/solved.html',{'question_list':question_list})

# # 零回答问题页
# class questionNoAnswerView(View):
#     def get(self,request):
#         question_list = Question.objects.filter(answer_count=0).order_by('-create_time')
#         return render(request,'question/noanswer.html',{'question_list':question_list})
    
# # 新评论问题页
# class questionNewComment(View):
#     def get(self,request):
#         comment_list = commentAnswer.objects.all().order_by('-create_time')
#         return render(request,'question/newcomment.html',{'comment_list':comment_list})
    
# # 新回答问题页
# class questionNewAnswer(View):
#     def get(self,request):
#         answer_list = Answer.objects.all().order_by('-create_time')
#         return render(request,'question/newanswer.html',{'answer_list':answer_list})

# # class questionHighscore(View):
# #     def get(self,request):
# #         question_list = Question.objects.filter()

# # 详细问题
# class questionDetailView(View):
#     def get(self,request,pk):
#         try:
#             question_obj = Question.objects.get(pk=pk)
#         except Exception as e:
#             question_obj = None
#         return render(request,'question/detail.html',{'question':question_obj})
    

# #回答问题
# class addAnswerView(View):
#     def post(self,request):
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             content = form.cleaned_data.get('content')
#             author_id = form.cleaned_data.get('author')
#             question_id = form.cleaned_data.get('question')
#             Answer.objects.create(content=content,author_id=author_id,question_id=question_id)
#             return redirect('/')
#         else:
#             return JsonResponse({"code":400,"msg":"参数错误!"})
      
        
# # 评论
# class addCommentView(View):
#     def post(self,request):
#         form = commentForm(request.POST)
#         if form.is_valid():
#             content = form.cleaned_data.get('content')
#             user_id = form.cleaned_data.get('user')
#             answer_id = form.cleaned_data.get('answer')
#             parent_id = form.cleaned_data.get('parent')
#             Answer.objects.create(content=content,user_id=user_id,answer_id=answer_id,parent_comment_id=parent_id)
#             return redirect('/')
#         else:
#             return JsonResponse({"code":400,"msg":"参数错误!"})
        
        
# # Home 家
# class homeView(View):
#     def get(self,request):
#         return render(request,'home/index.html',{})
        
            
            
# # Home 博客
# class homeBlogIndexView(View):
#     def get(self,request):
#         current_page = request.GET.get('page',1)
#         article_list = Article.objects.all().order_by('-create_time')
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
        
#         return render(request,'home/blog.html',{'article_list':page_article_obj,'page_list':page_list})
    
    
# # 我推荐的博客文章
# class homeBlogMyDiggView(View):
#     def get(self,request):
#         current_page = request.GET.get('page',1)
#         article_list = Article.objects.all().order_by('-create_time')
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
        
#         return render(request,'home/blog.html',{'article_list':page_article_obj,'page_list':page_list})
    

# # 我评论的博客文章
# class homeBlogMyCommentedView(View):
#     def get(self,request):
#         current_page = request.GET.get('page',1)
#         article_list = Article.objects.all().order_by('-create_time')
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
        
#         return render(request,'home/blog.html',{'article_list':page_article_obj,'page_list':page_list})
    
    
# # Group 小组
# class groupIndexView(View):
#     def get(self,request):
#         pass
    

# # 小组发言
# class groupSpeechView(View):
#     def post(self,request):
#         pass
    
    
# # 后台管理页面
# class cnBackEndView(LoginRequiredMixin,View):
#     def get(self,request,username):
#         current_page = request.GET.get('page')
#         user_obj = User.objects.filter(username=username).exists()
#         # 判断用户是否存在
#         if not user_obj:
#             return JsonResponse({'code':400,'msg':"not found"})
#         # 该用户后台文章列表
#         article_list = Article.objects.filter(user=user_obj)
        
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
        
#         return render(request,'blog/backend.html',{
#             'articleList':page_article_obj,
#             'pageList':page_list,
#             })
    

# # 添加文章
# class addArticleView(LoginRequiredMixin,View):
#     def get(self,request):
#         return render(request,'blog/add_article.html',{})
    
#     def post(self,request):
#         form = addEditArticleForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get('content')
            
#             Article.objects.create(title=title,content=content,user=request.user)
            
#             return redirect('/cn_backend/')
#         else:
#             return JsonResponse({'code':400,"message":"参数错误"})
    
    
# # 编辑文章
# class editArticleView(LoginRequiredMixin,View):
#     def post(Self,request):
#         article_form = addEditArticleForm(request.POST)
#         if article_form.is_valid():
#             pass
    
    
# # 删除文章
# class delArticleView(LoginRequiredMixin,View):
#     def post(self,request,pk):
#         Article.objects.filter(id=pk).delete()
#         return redirect('/')


