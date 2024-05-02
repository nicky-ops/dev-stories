from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.views.decorators.http import require_POST

# Create your views here.
def post_list(request):
    """
    Return a list of posts that are published
    """
    # Get all posts ordered by publish date
    posts = Post.published.all().order_by('-publish')
    
    # Get popular posts
    popular_posts = Post.published.get_popular_posts()
    
    # Get recent posts (let's say the 5 most recent ones)
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
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form, 'comment': comment})
