from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, CreatePostForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    """
    Return a list of posts that are published
    """
    posts = Post.published.all()
    # Get popular posts
    popular_posts = Post.published.get_popular_posts()
    recent_posts = Post.published.all().order_by('-publish')[:5]
    return render(request, 'blog/post/list.html', {'posts': posts, 'popular_posts': popular_posts, 'recent_posts': recent_posts})

def post_detail(request, id):
    """
    Post detail view
    """
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'form': form})

@require_POST
@login_required
def post_comment(request, post_id):
    """
    Handles comment submissions on a blog post
    """
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author_id = 1  # Replace with actual author id
        comment.save()
        return redirect('blog:post_detail', id=post_id)
    else:
        comments = post.comments.filter(active=True)
    return render(request, 'blog/post/detail.html', {'post': post, 'form': form, 'comment': comment})

@login_required
def create_post(request):
    """
    Create a new post
    """
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_list')
    else:
        form = CreatePostForm()
    return render(request, 'blog/post/create.html', {'form': form})

def about_page(request):
    return render(request, 'blog/about.html')
