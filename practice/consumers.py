from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from _thread import start_new_thread

class PracticeConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'TicTacToeConsumer'
        self.room_group_name = 'GET_Data';

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        ) 
        self.accept()

    def disconnect(self, close_code):
        print("Disconnected")
        # Leave room group
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        # text_data_json = json.loads(text_data)
        print(text_data)
        start_new_thread(self.send_message, (text_data,))

    def send_message(self, text):
        """ Receive message from room group """
        print(text)
         
        try:
            val = json.dumps(text["value"])
            print(val)
            self.send(text_data = val,)
        except:
            self.send(text_data = json.dumps({'payload':text}))
