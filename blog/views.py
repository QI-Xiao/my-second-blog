from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Post
from .forms import PostForm, UserForm
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            usernames = uf.cleaned_data['username']
            print(usernames)
            passwords = uf.cleaned_data['password']
            passwordsagain = uf.cleaned_data['passwordagain']
            print(passwords)
            # if usernames and passwords:
            #     registerAdd = User.objects.get_or_create(username=usernames, password=passwords)
            #     if created:
            if passwords != passwordsagain:
                print('fggggggggggg')
                return render(request, 'blog/register.html', {
                    'uf':uf,
                    'error_message':'密码不一致',
                })
            if User.objects.filter(username=usernames): # 存在
                print('a')
                return render(request, 'blog/register.html', {
                    'uf': uf,
                    'error_message':'用户名已存在',
                })
            else:  # 不存在
                User.objects.create_user(username=usernames, password=passwords)
                print('bbbbbbbbbbbbb')
                # user = authenticate(request, username=usernames, password=passwords)
                # login(request, user)
                do_login(request)
                return HttpResponseRedirect(reverse('post_list'))
    else:
        uf = UserForm()
        print('55555555555555555')
    return render(request, 'blog/register.html', {'uf': uf})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('post_list'))


def do_login(request):
    if request.method == 'GET':
        print('1234567')
        return render(request, 'blog/login.html')
    print('22222222222222222')
    usernames = request.POST.get('username', "")
    print(usernames)
    password = request.POST.get('password', "")
    print(password)

    user = authenticate(request, username=usernames, password=password)
    if user is not None:
        login(request, user)
        print('333333333333')
        return HttpResponseRedirect(reverse('post_list'))
    else:
        print('4444444444444')
        return render(request, 'blog/login.html',{
            'username': '',
            'password': '',
            'error_message': '用户名或密码错误',
        })
# if request.user.is_authenticated():
#     # Do something for authenticated users.
# else:
#     # Do something for anonymous users.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_new(request):
    if request.method == "POST":
        print('method is post!!!!!!!!!')
        form = PostForm(request.POST)
        if form.is_valid():
            print('bbbbbbbbbbbbbbbbbbbbbbbbbbb')
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        print('ccccccccccccccccccccccccccccc')
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        if request.method == 'POST':
            print('dddddddddddddddd')
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                print('eeeeeeeeeeeeeeeee')
                post = form.save(commit=False)
                print('111111111111')
                # post.author = request.user
                print('222222222222')
                post.published_date = timezone.now()
                post.save()
                print('33333333333')
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
            print('ffffffffffffffffffffff')
        return render(request, 'blog/post_edit.html', {'form': form})
    return HttpResponseRedirect(reverse('post_detail', args=(pk,)))
