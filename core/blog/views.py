from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from blog.models import Post , Category

# Blog view
def blog_view(request, **fields):
    """ Summary:
        - A function for showing posts. Fields are the kwargs and
          used for getting extra fields(like category) and search
          the posts that contains these fields and show them to a
          user.
        - Use paginator to paginate posts.
    """
    posts = Post.objects.filter(status=True)
    categories = Category.objects.annotate(post_count=Count("post"))
    total_post_count = posts.count()
    
    if fields.get("cat_name") != None:
        posts = Post.objects.filter(categories__name = fields["cat_name"])
        
    if fields.get("author_user") != None:
        posts = Post.objects.filter(photographer__username = fields["author_user"])
        
    if fields.get("tag_name") != None:
        posts = Post.objects.filter(tags__name__in = [fields["tag_name"]])
    
    # Pagination
    posts = Paginator(posts, 9)
    try:
        page_num = request.GET.get('page')
        posts = posts.get_page(page_num)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    
    context = {
        "posts": posts,
        "categories": categories,
        "total_posts": total_post_count
    }
    return render(request, "blog/blog-home.html", context)

def detail_view(request, name):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, title=name)
    context = {"post" : post}
    return render(request, "blog/blog-detail.html", context)

