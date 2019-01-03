from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class GenericConsumer(WebsocketConsumer):
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
        message = text_data_json['message']
        parameter = text_data_json['parameter']
        if 'name' in text_data_json:
            name = text_data_json['name']
        else:
            name = self.scope['user'].username.title()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'new_data',
                'message': message,
                'parameter': parameter,
                'name': name,
            }
        )

    # Receive message from room group
    def new_data(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': event['message'],
            'parameter': event['parameter'],
            'name': event['name'],
        }))
