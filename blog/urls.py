from django.urls import path
from .views import home, post_detail, PostListView

urlpatterns = [
    path('home/', home, name='home'),
    path('post/<slug:slug>', post_detail, name='post_detail'),
    path('list/', PostListView.as_view(), name='list'),
]