import asyncio
import json
import logging
import websockets


logging.basicConfig()

BOARD_CONTENT = {'content': ''}
PARTICIPANTS = set()

def state_event():
    return json.dumps({'type': 'state', **BOARD_CONTENT})

def participant_event():
    return json.dumps({'type': 'users', 'pariticipant_id': ['1','2','3']})

async def notify_state():
    if PARTICIPANTS:      
        message = state_event()
        await asyncio.wait([participant.send(message) for participant in PARTICIPANTS])

async def notify_participants():
    if PARTICIPANTS:      
        message = participant_event()
        await asyncio.wait([participant.send(message) for participant in PARTICIPANTS])

async def register(websocket):
    PARTICIPANTS.add(websocket)
    await notify_participants()

async def unregister(websocket):
    PARTICIPANTS.remove(websocket)
    await notify_participants()

async def counter(websocket, path):

    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            print(data)
            if data['user_type'] == 'host':
                BOARD_CONTENT['content'] = data['content']
                BOARD_CONTENT['cursor_position'] = data['cursor_position']
                print(BOARD_CONTENT)
                await notify_state()
            else:
                logging.error(
                    "unsupported event: {}", data)
    finally:
        await unregister(websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(counter, 'localhost', 8848))
asyncio.get_event_loop().run_forever()