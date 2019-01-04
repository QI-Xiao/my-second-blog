from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post # 哪个模型会被用来创建这个表单
        fields = ('title', 'text',) # 哪些字段会在我们的表单里出现


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100, widget=forms.TextInput(attrs={'placeholder':'用户名', 'class':'form-control'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'placeholder':'密码', 'class':'form-control'}))
    passwordagain = forms.CharField(label='再次输入密码', widget=forms.PasswordInput(attrs={'placeholder':'确认密码', 'class':'form-control'}))
