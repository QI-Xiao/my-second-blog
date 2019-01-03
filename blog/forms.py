from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post # 哪个模型会被用来创建这个表单
        fields = ('title', 'text',) # 哪些字段会在我们的表单里出现


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100, widget=forms.TextInput(attrs={'placeholder':'请输入用户名'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'placeholder':'请输入密码'}))
    passwordagain = forms.CharField(label='再次输入密码', widget=forms.PasswordInput(attrs={'placeholder':'请重复密码'}))
