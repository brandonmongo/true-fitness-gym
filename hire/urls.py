from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_PTs, name='all_PTs'),
    path('detail/<PT_slug>/', views.PTs_details, name='PTs_details'),
    path('add/', views.add_PT, name='add_pt')
]
