from django.urls import path
from . import views

urlpatterns = [
    path("", views.startingpage, name = 'startingpage'),
    path('posts/', views.posts, name = 'posts'),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name = 'post_details'),
    path('read-later', views.ReadLaterView.as_view(), name="read-later"),
]