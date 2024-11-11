from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_posts': page_obj})