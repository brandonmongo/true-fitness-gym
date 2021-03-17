from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostList.as_view, name='blog'),
    path('<slug>/', views.PostDetail.as_view(), name='post_details'),
]