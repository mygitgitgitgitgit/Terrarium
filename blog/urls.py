from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sub', views.sub_html, name='sub'),
    path('dev_html', views.dev_html, name='dev_merge')
]