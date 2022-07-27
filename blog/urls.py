from django.urls import path
from . import views

app_name = "blog"


urlpattern = [
    path("", views.PostListView.as_view(), name="all"), path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("update/<slug:slug>", views.PostUpdateView.as_view(), name="post_update"),
    path("delete/<slug:slug>", views.PostDeleteView.as_view(), name="post_delete"),
    path("read/<slug:slug>", views.PostDetailView.as_view(), name = "post_detail")]
