from django.urls import path
from . import views


app_name = "blogs"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
    path("post/new/", views.PostCreateView.as_view(), name="create"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
]
