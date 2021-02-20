from django.urls import path
from . import views
urlpatterns = [
    path('', views.true_products, name='products'),
    path('<product_id>', views.true_product_details, name='products_details')
]
