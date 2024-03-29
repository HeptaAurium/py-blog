from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/create/", views.createBlog, name="createBlog")
]