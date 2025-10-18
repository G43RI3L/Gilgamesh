from fastapi import Request
from fastapi.responses import StreamingResponse
import asyncio
import json

subscribers = []

async def event_generator():
    q = asyncio.Queue()
    subscribers.append(q)
    try:
        while True:
            data = await q.get()
            yield f"data: {json.dumps(data)}\n\n"
    except asyncio.CancelledError:
        subscribers.remove(q)
        raise

def publish_event(data):
    for q in list(subscribers):
        try:
            q.put_nowait(data)
        except Exception:
            pass
