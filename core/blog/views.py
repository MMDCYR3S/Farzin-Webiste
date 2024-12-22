from django.shortcuts import render

# Blog view
def blog_view(request):
    return render(request, "blog/blog-home.html")

def detail_view(request):
    return render(request, "blog/blog-detail.html")
