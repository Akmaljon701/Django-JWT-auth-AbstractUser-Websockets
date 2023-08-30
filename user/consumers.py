from .serializers import *


from asgiref.sync import sync_to_async
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Ism


class IsmlarConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("ism_group", self.channel_name)
        await self.send_initial_ism_list()

    async def disconnect(self, close_code):
        pass

    async def send_initial_ism_list(self):
        ism_list = await self.get_ism_list()
        await self.send(text_data=json.dumps(ism_list))

    async def add_new_ism(self, event):
        await self.send_initial_ism_list()

    @sync_to_async
    def get_ism_list(self):
        ism_objects = Ism.objects.all().order_by('-id')
        serializer = IsmSerializer(ism_objects, many=True)
        return serializer.data
