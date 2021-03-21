from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_PTs, name='all_PTs')
]
