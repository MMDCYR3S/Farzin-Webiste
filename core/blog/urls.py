from django.urls import path
from blog.views import(
    blog_view,
    detail_view
)

# app_name to recognize urls
app_name = "blog"

urlpatterns = [
    path("", blog_view, name="blog"),
    path("post/", detail_view, name="blog-detail"),
]