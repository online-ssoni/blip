import asyncio
import json
import logging
import websockets
from django.core.management.base import BaseCommand, CommandError

BOARD_CONTENT = {'content': '','session_id':1234, 'content_type':'', 'board_state':'', 'toggle':'pristine'}
CHAT_MESSAGE = {'message':'','session_id':1234}
PARTICIPANTS = set()


class Command(BaseCommand):
    help = 'Runs Websocket Server'

    logging.basicConfig()

    def state_event(self):
        return json.dumps({'type': 'state', **BOARD_CONTENT})

    def participant_event(self):
        return json.dumps({'type': 'users', 'pariticipant_id': ['1','2','3']})

    async def notify_state(self):
        if PARTICIPANTS:      
            message = self.state_event()
            await asyncio.wait([participant.send(message) for participant in PARTICIPANTS])

    async def notify_participants(self):
        if PARTICIPANTS:      
            message = self.participant_event()
            await asyncio.wait([participant.send(message) for participant in PARTICIPANTS])

    async def register(self, websocket):
        PARTICIPANTS.add(websocket)
        await self.notify_participants()

    async def unregister(self, websocket):
        PARTICIPANTS.remove(websocket)
        await self.notify_participants()

    async def counter(self, websocket, path):
        await self.register(websocket)
        try:
            await websocket.send(self.state_event())
            async for message in websocket:
                data = json.loads(message)
                if data['type'] == 'chat':
                    CHAT_MESSAGE['message'] = data['message']
                    await self.broadcast_message()
                elif data['type'] == 'board':
                    if data['user_type'] == 'host':
                        BOARD_CONTENT['content_type'] = data['content_type']           
                        BOARD_CONTENT['content'] = data['content']
                        if BOARD_CONTENT['content_type'] == 'code':
                            BOARD_CONTENT['cursor_position'] = data['cursor_position']
                            BOARD_CONTENT['board_state'] = data['board_state']
                        if 'toggle' in data and data['toggle'] == 'dirty': 
                            BOARD_CONTENT['toggle']='dirty'
                        else:
                            BOARD_CONTENT['toggle']='pristine'
                        await self.notify_state()
                else:
                    logging.error("Unsupported{}", data)
        finally:
            await self.unregister(websocket)

    def handle(self, *args, **options):
            asyncio.get_event_loop().run_until_complete(websockets.serve(self.counter, 'localhost', 8848))
            asyncio.get_event_loop().run_forever()  