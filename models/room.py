from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from database import Base

# Room model for collaborative coding room
class Room(Base):
    __tablename__ = 'rooms'


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # Uid for  room
    name = Column(String(128), nullable=True)
    code = Column(Text, default='')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    



