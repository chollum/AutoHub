from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='chatselect'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
