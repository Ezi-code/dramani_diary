from django.urls import path
from . import views


app_name = "blogs"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("posts/search/", views.SearchView.as_view(), name="search"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
    path("posts/new/", views.PostCreateView.as_view(), name="create"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="update"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),

]
