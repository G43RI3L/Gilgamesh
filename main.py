from fastapi import FastAPI
from app.db import init_db
from app.api import products, movements, chat
from app.utils.sse import event_generator
from fastapi.responses import StreamingResponse

app = FastAPI()
app.include_router(products.router)
app.include_router(movements.router)
app.include_router(chat.router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/events")
async def sse():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
