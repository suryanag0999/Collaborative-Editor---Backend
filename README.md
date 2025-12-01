# Collaborative Editor 
- A simplified real-time programming web application where  two users can join a room and collaboratively edit code. 

## Git Repository Structure
'''collab-editor/
│
├── backend/                     # FastAPI backend
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── room.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── rooms.py
│   │   └── autocomplete.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── room_service.py
│   └── websocket/
│       ├── __init__.py
│       └── manager.py
├── .env                         # Database config
├── requirements.txt             # Python dependencies
└── README.md
'''
### Project Structure
**backend/** – FastAPI project
  - **main.py** – Entry point
  - **database.py** – SQLAlchemy DB setup
  - **models/** – SQLAlchemy models
  - **routers/** – REST API endpoints
  - **services/** – Business logic (create room, update code)
  - **websocket/** – WebSocket manager for real-time collaboration

#### Setup & Run
1. Install dependencies:
cd backend
pip install -r requirements.txt

2.   Configure PostgreSQL .env:
DATABASE_URL=postgresql://postgres:<password>@localhost:5432/collab_db
HOST=127.0.0.1
PORT=8000

3.  Initialize DB:
from database import init_db
init_db()

4.  Run backend:
uvicorn main:app --reload or fastapi dev main.py


5. API docs: 
http://127.0.0.1:8000/docs 
 

#### Architecture & Design Choices
- FastAPI for REST endpoints and WebSockets
- PostgreSQL + SQLAlchemy for persistent room/code storage
- WebSocket manager maintains:
- Active connections per room
- In-memory last-known code cache
- AI Autocomplete  is a simple rule-based suggestion engine

##### How to Test

1. Create a room:
POST /rooms
{
  "name": "Test Room"
}
- Response includes a roomId

2. Connect multiple clients using frontend/index.html or WebSocket client:
ws://127.0.0.1:8000/ws/<roomId>
- Typing updates appear in real-time between clients




3. Test /autocomplete endpoint 
POST /autocomplete
{
  "code": "pri",
  "cursorPosition": 3,
  "language": "python"
}



