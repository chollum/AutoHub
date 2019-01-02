from django.urls import path
from . import views

urlpatterns = [
    path('doors/', views.doors, name='doors'),
    path('lights/', views.lights, name='lights'),
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
]
