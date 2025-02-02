from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def sub_html(request):
    return render(request, 'sub_html.html')
def dev_html(request):
    return render(request, 'dev_html.html')
