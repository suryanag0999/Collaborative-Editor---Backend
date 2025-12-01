from sqlalchemy.orm import Session
from models.room import Room
import uuid

# room managment functions
def create_room(db: Session, name: str | None = None) -> str:
    r = Room(name=name)
    db.add(r)
    db.commit()
    db.refresh(r)
    return str(r.id)



def get_room(db: Session, room_id: str) -> Room | None:
    try:
        uid = uuid.UUID(room_id)
    except Exception:
        return None
    return db.query(Room).filter(Room.id == uid).first()
    



def update_room_code(db: Session, room_id: str, code: str) -> bool:
    r = get_room(db, room_id)
    if not r:
        return False
    r.code = code
    db.add(r)
    db.commit()
    return True





#for createing room
"""
    Create a new Room in the database.

    Args:
        db (Session): SQLAlchemy database session
        name (str | None): Optional room name

    Returns:
        str: UUID of the created room
    """

#for getting room details

"""
    Retrieve a Room by its UUID.

    Args:
        db (Session): SQLAlchemy database session
        room_id (str): UUID string of the room

    Returns:
        Room | None: Room object if found, else None
    """
# for updateing deails
"""
    Update the code of an existing room.

    Args:
        db (Session): SQLAlchemy database session
        room_id (str): UUID string of the room
        code (str): Code content to update

    Returns:
        bool: True if update successful, False if room not found
    """
