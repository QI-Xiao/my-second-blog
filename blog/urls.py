from django.urls import path

from . import views

urlpatterns = [
    path(r'blog/', views.post_list, name='post_list'),
]
