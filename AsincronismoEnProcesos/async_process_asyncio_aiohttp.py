import asyncio
from flask import Flask, jsonify
from aiohttp import ClientSession

app = Flask(__name__)

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()

async def get_async_data():
    async with ClientSession() as session:
        tasks = [fetch('https://jsonplaceholder.typicode.com/posts/1', session),
                 fetch('https://jsonplaceholder.typicode.com/posts/2', session)]
        results = await asyncio.gather(*tasks)
        return results

@app.route('/get_async_data', methods=['GET'])
def get_async_data_route():
    loop = asyncio.get_event_loop()
    try:
        results = loop.run_until_complete(get_async_data())
        return jsonify(results)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()