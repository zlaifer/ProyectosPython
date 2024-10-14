# server.py
import asyncio
import websockets
import json

async def echo(websocket, path):
    print('llego algo')
    async for message in websocket:
        data = json.loads(message)
        delay = data.get('delay', 0)
        await asyncio.sleep(delay)
        await websocket.send(f"Received after {delay} seconds: {data['message']}")

start_server = websockets.serve(echo, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
