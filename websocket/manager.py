from fastapi import WebSocket
from typing import Dict, Set, Optional
import json
from services.room_service import update_room_code
from database import SessionLocal


class ConnectionManager:
    def __init__(self):
        # map room_id to set(WebSocket)
        self.active: Dict[str, Set[WebSocket]] = {}
        # in-memory lastknown code asper room
        self.room_code_cache: Dict[str, str] = {}



async def connect(self, room_id: str, websocket: WebSocket):
    await websocket.accept()
    conns = self.active.setdefault(room_id, set())
    conns.add(websocket)


def disconnect(self, room_id: str, websocket: WebSocket):
    conns = self.active.get(room_id)
    if conns and websocket in conns:
        conns.remove(websocket)
        if not conns:
            #  clear memory cache
            self.room_code_cache.pop(room_id, None)



async def broadcast_update(self, room_id: str, data: dict, sender: Optional[WebSocket] = None):
    # persist code if provided
    if 'code' in data and isinstance(data['code'], str):
        self.room_code_cache[room_id] = data['code']
        db = None
        try:
            db = SessionLocal()
            update_room_code(db, room_id, data['code'])
        except Exception:
            pass
        finally:
            if db:
                try:
                    db.close()
                except Exception:
                    pass


    conns = set(self.active.get(room_id) or set())
    text = json.dumps(data)
    for conn in list(conns):
        if conn == sender:
            continue
        try:
            await conn.send_text(text)
        except Exception:
            try:
                conns.remove(conn)
            except Exception:
                pass


manager = ConnectionManager()
