from django.urls import path
from blog.views import(
    blog_view,
    detail_view,
)

# app_name to recognize urls
app_name = "blog"

urlpatterns = [
    path("", blog_view, name="blog"),
    path("<str:name>", detail_view, name="blog-detail"),
    path("cat/<str:cat_name>", blog_view, name="category"),
    path("author/<str:author_user>", blog_view, name="author"),
    path("tag/<str:tag_name>", blog_view, name="tag"),
]