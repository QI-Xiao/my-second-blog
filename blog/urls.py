from django.urls import path, re_path

from . import views

# app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    path('do_login/', views.do_login, name='do_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    re_path(r'^post/(?P<pk>[0-9]+)/comment/$', views.comment_on, name='comment_on'),
    re_path(r'^post/(?P<pk>[0-9]+)/like/$', views.click_like, name='click_like'),
    re_path(r'^post/(?P<pk>[0-9]+)/delcomment/$', views.del_comment, name='del_comment'),
]


