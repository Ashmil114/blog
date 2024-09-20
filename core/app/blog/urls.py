from django.urls import path
from .views import (
    home,
    about,
    post_detail,
    post,
    add_post,
    delete_post,
    edit_post,
    add_category,
)

urlpatterns = [
    path("", home, name="home"),
    path("post/<slug:pk>", post_detail, name="post_detail"),
    path("post", post, name="post"),
    path("add-post", add_post, name="add_post"),
    path("add-category", add_category, name="add_category"),
    path("delete-post/<slug:pk>", delete_post, name="delete_post"),
    path("edit-post/<slug:pk>", edit_post, name="edit_post"),
    path("about", about, name="about"),
]
