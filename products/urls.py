from django.urls import path
from . import views
urlpatterns = [
    path('', views.true_products, name='products'),
    path('<int:product_id>/', views.true_product_details, name='products_details'),
    path('add/', views.add_product, name='add_product')
]
