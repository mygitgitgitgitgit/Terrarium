from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('dev_html', views.dev_html, name='dev_merge')
]