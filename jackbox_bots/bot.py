import jackbox
import asyncio
import threading
import time
import sys

def Bot():
    def __init__(self, name):
        self.client = jackbox.Client()
        self.name = name

    async def connect(self, room_id: str, name: str):
        await self.client.connect(room_id, name)


