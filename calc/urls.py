from django.urls import path
from . import views
urlpatterns=[
path('', views.home, name='home'),
path('add',views.add, name='add'),
path('dashboard/',views.dashboard, name='dashboard'),
path('pricing/',views.pricing, name='pricing'),
path('features/',views.features, name='features'),
path('settings/',views.settings, name='settings'),
]