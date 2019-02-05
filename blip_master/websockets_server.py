import asyncio
import json
import logging
import websockets


logging.basicConfig()

BOARD_CONTENT = {'content': '','session_id':1234, 'content_type':'', 'board_state':'', 'toggle':'pristine'}
CHAT_MESSAGE = {'message':'','session_id':1234}
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

async def broadcast_message():
   if PARTICIPANTS:
       message =  json.dumps({'type': 'chat', **CHAT_MESSAGE})
       await asyncio.wait([participant.send(message) for participant in PARTICIPANTS])


async def counter(websocket, path):
   await register(websocket)
   try:
       await websocket.send(state_event())
       async for message in websocket:
           data = json.loads(message)
           if data['type'] == 'chat':
               CHAT_MESSAGE['message'] = data['message']
               await broadcast_message()
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
                   await notify_state()
           else:
               logging.error("UNsopported{}", data)
   finally:
       await unregister(websocket)
asyncio.get_event_loop().run_until_complete(
   websockets.serve(counter, 'localhost', 8848))
asyncio.get_event_loop().run_forever()