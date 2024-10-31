from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout


from utils.mixin_utils import LoginRequiredMixin
from .forms import LoginForm,RegisterForm
from users.models import User,CaptchaModel
from utils.email_send import send_email


import json


# 注册
class registerView(View):
    def get(self,request):
        return render(request,'register.html')
    
    
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            User.objects.create_user(email=email, username=username, password=password)
            return HttpResponseRedirect('/login')
        else:
            print(register_form.errors)
            return HttpResponseRedirect('/register')
   
        
#登录
class loginView(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                # 登录
                login(request, user)
                # 判断是否需要记住我
                if not remember:
                    # 如果没有点击记住我，那么就要设置过期时间为0，即浏览器关闭后就会过期
                    request.session.set_expiry(0)
                return HttpResponseRedirect('/')
            else:
                print('邮箱或密码错误！')
                return HttpResponseRedirect('/login')
        else:
            return HttpResponseRedirect('/login')
    

# 退出登录
class logoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')
    
    
# 发送邮件获取验证码
def sendCaptcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code':400,"message":"您还没有输入邮箱!"})
    send_email(email=email,send_type='register')
    return JsonResponse({'code':200,'message':"您的邮箱验证码发送成功!"})