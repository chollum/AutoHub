from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/hub/data', consumers.DataConsumer),
    url(r'^ws/hub/doors', consumers.DataConsumer),
#    url(r'^ws/hub/chat', consumers.GenericConsumer),
]
