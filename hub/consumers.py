from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Room

class DataConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope['path'].strip('/').split('/')[-1]
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        value = text_data_json['value']
        parameter = text_data_json['parameter']
        if 'tag' in text_data_json:
            tag = text_data_json['tag']
        else:
            tag = self.scope['user'].username.title()

        try:
            r = Room.objects.get(tag=tag)
        except Room.DoesNotExist:
            r = Room(tag=tag)
        if parameter in ['temperature','humidity','description']:
            setattr(r, parameter, value)
        r.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'id': r.id,
                'type': 'new_data',
                'value': value,
                'parameter': parameter,
                'tag': tag,
            }
        )

    # Receive message from room group
    def new_data(self, event):
        # Send message to WebSocket
        data = {
            'id': event['id'],
            'value': event['value'],
            'parameter': event['parameter'],
            'tag': event['tag'],
        }
        self.send(text_data=json.dumps(data))

