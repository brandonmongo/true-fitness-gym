from django.urls import path
from . import views
urlpatterns = [
    path('', views.true_products, name='products')
]