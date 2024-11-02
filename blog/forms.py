from django import forms

# 个人博客文章
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=32, min_length=2)
    content = forms.CharField(min_length=2)
    category = forms.IntegerField()
    tags = forms.CharField()
    

# 个人博客标签
class TagForm(forms.Form):
    title = forms.CharField(max_length=32, min_length=2)
    
    