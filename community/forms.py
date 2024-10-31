from django import forms

# from .models import Question

        
# class QuestionForm(forms.Form):
#     title = forms.CharField(required=True,min_length=2)
#     content = forms.CharField(required=True)
#     author = forms.CharField(required=True)
#     tags = forms.CharField(min_length=2)
#     is_draft = forms.BooleanField(required=True)
#     reward = forms.IntegerField()
 
    
# class AnswerForm(forms.Form):
#     content = forms.CharField(required=True,min_length=10)
#     question = forms.IntegerField(required=True)
#     author = forms.IntegerField(required=True)
    

# class commentForm(forms.Form):
#     content = forms.CharField(required=True,min_length=2)
#     user = forms.IntegerField(required=True)
#     answer = forms.IntegerField(required=True)
#     parent = forms.IntegerField(required=True)

class blogRegisterForm(forms.Form):
    sub_url = forms.CharField(required=True)
    theme = forms.CharField(required=True)
    
# class addEditArticleForm(forms.Form):
#     title = forms.CharField(max_length=64)
#     content = forms.CharField(min_length=2)