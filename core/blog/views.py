from django.shortcuts import render, get_object_or_404
from blog.models import Post , Category

# Blog view
def blog_view(request, **fields):
    """ Summary:
        - A function for showing posts. Fields are the kwargs and
          used for getting extra fields(like category) and search
          the posts that contains these fields and show them to a
          user.
    """
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    
    if fields.get("cat_name") != None:
        posts = Post.objects.filter(categories__name = fields["cat_name"])
        
    if fields.get("author_user") != None:
        posts = Post.objects.filter(photographer__username = fields["author_user"])
        
    if fields.get("tag_name") != None:
        posts = Post.objects.filter(tags__name__in = [fields["tag_name"]])
    
    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "blog/blog-home.html", context)

def detail_view(request, name):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, title=name)
    context = {"post" : post}
    return render(request, "blog/blog-detail.html", context)

