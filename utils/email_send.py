import random
import string
from django.core.mail import send_mail

from users.models import CaptchaModel
from LAMDA.settings import EMAIL_FROM
   
        
        
def send_email(email,send_type='register'):
    code = "".join(random.sample(string.digits,6))
    CaptchaModel.objects.create(code=code,email=email,send_type=send_type)
    
    # 定义邮件内容
    email_title = ""
    email_body = ""
    
    if send_type == "register":
        email_title = "LAMDA社区注册"
        email_body = f"你注册的验证码为{code}"

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，从哪里发，接受者list
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "LAMDA社区找回密码"
        email_body = f"您找回密码的验证码为{code}"

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，从哪里发，接受者list
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = "LAMDA社区邮箱修改验证码"
        email_body = "你的邮箱验证码为{0}".format(code)

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，从哪里发，接受者list
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            pass