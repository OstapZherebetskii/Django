from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.index, name='home'),
  path('about/', views.about, name='about'),
  path('orders/', views.orders, name='orders'),
  path('new_order/', views.new_order, name='new_order'),
  path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
  path('delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),

]