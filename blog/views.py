from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

"""
post_list という関数（def から始まる部分のことです）を作りました。これは request を引数に取ります。
blog/post_list.html テンプレートを（色々なものを合わせて）組み立てる render という関数を呼び出して得た値を return しています。
"""