from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from routers import rooms as rooms_router
from routers import autocomplete as autocomplete_router
from websocket.manager import manager
import json
from fastapi.middleware.cors import CORSMiddleware
from database import init_db

#fast api app instance
app = FastAPI(title='Collaborative Editor - Backend')


# init DB
init_db()

# allowing cors 
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],   # allow requests from any origin
allow_credentials=True,
allow_methods=["*"],   # allow all httP methods
allow_headers=["*"],   # allow all headers

)

#include aPi routes
app.include_router(rooms_router.router)
app.include_router(autocomplete_router.router)


@app.websocket('/ws/{room_id}')
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(room_id, websocket)
    initial = manager.room_code_cache.get(room_id)
    if initial is not None:
        await websocket.send_text(json.dumps({"type": "init", "code": initial}))
    try:
        while True:
            text = await websocket.receive_text()
            try:
                data = json.loads(text)
            except Exception:
                data = {"type": "raw", "text": text}
            if isinstance(data, dict) and data.get('type') == 'update':
                await manager.broadcast_update(room_id, data, sender=websocket)
            else:
                await manager.broadcast_update(room_id, data, sender=websocket)
    
    except WebSocketDisconnect: #disconncet active connections
        manager.disconnect(room_id, websocket)


