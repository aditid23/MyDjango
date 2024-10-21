from django.urls import path
from . import views
urlpatterns=[
path('', views.home, name='home'),
path('add',views.add, name='add'),
path('dashboard/',views.dashboard, name='dashboard'),
path('pricing/',views.pricing, name='pricing'),
path('features/',views.features, name='features'),
path('settings/',views.settings, name='settings'),
path('products/',views.products, name='products'),
path('customer/<str:pk_test>/',views.customer, name='customer'),
path('create_order/',views.createOrder, name='create_order'),
path('update_order/<str:pk>/',views.updateOrder, name='update_order'),
path('orderpage',views.orderpage, name='orderpage'),
path('delete_order/<str:pk>/',views.deleteOrder, name='delete_order'),
path('register/',views.register, name='register'),
path('login/',views.loginPage, name='login'),
path('logout/',views.logoutPage, name='logout'),
path('insertData',views.insertData, name='insertData'),
]