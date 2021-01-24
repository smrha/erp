from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status='p')
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj
    }
    return render(request, 'blog/blog-list.html', context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post,
                                   status = 'p',
                                   publish__year = year,
                                   publish__month = month,
                                   publish__day = day)
    context = {
        'post': post
    }
    return render(request, 'blog/post-detail.html', context)