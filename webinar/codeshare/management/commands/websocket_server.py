import asyncio
import json
import logging
import websockets
from django.core.management.base import BaseCommand, CommandError


BOARD_CONTENT = {'content': ''}
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
                print(data)
                if data['user_type'] == 'host':
                    BOARD_CONTENT['content'] = data['content']
                    BOARD_CONTENT['cursor_position'] = data['cursor_position']
                    print(BOARD_CONTENT)
                    await self.notify_state()
                else:
                    logging.error(
                        "unsupported event: {}", data)
        finally:
            await self.unregister(websocket)

    def handle(self, *args, **options):
        asyncio.get_event_loop().run_until_complete(websockets.serve(self.counter, 'localhost', 8848))
        asyncio.get_event_loop().run_forever()