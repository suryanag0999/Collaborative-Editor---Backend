from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, init_db
import models.room as room_model
from services.room_service import create_room, get_room


router = APIRouter()


# Ensure tat tables are created in prototype
init_db()


@router.post('/rooms')
def create_room_endpoint(payload: dict, db: Session = Depends(get_db)):
    name = payload.get('name')
    room_id = create_room(db, name)
    return {"roomId": room_id}



@router.get('/rooms/{room_id}')
def get_room_endpoint(room_id: str, db: Session = Depends(get_db)):
    r = get_room(db, room_id)
    if not r:
        raise HTTPException(status_code=404, detail='Room not found')
    return {"roomId": str(r.id), "code": r.code}
