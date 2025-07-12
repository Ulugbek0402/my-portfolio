from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_list, name='list'),
    path('add/', views.add_product, name='add'),
    path('<int:pk>/', views.product_detail, name='detail'),
    path('update/<int:pk>/', views.update_product, name='update'),
    path('delete/<int:pk>/', views.delete_product, name='delete'),
]
