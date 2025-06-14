# Event Management System API

A FastAPI-based Event Management System that allows users to register for events, track attendance, and manage event information and speaker details.

## Features

- User management (CRUD operations)
- Event management (CRUD operations)
- Speaker management
- Event registration and attendance tracking
- Validation and relationship management between entities

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the server:
```bash
uvicorn main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Users
- GET /users - List all users
- POST /users - Create a new user
- GET /users/{user_id} - Get user details
- PUT /users/{user_id} - Update user
- DELETE /users/{user_id} - Delete user
- PATCH /users/{user_id}/deactivate - Deactivate user

### Events
- GET /events - List all events
- POST /events - Create a new event
- GET /events/{event_id} - Get event details
- PUT /events/{event_id} - Update event
- DELETE /events/{event_id} - Delete event
- PATCH /events/{event_id}/close - Close event registration

### Registrations
- POST /registrations - Register for an event
- GET /registrations - List all registrations
- GET /registrations/user/{user_id} - Get user's registrations
- PATCH /registrations/{registration_id}/attend - Mark attendance

### Speakers
- GET /speakers - List all speakers
- GET /speakers/{speaker_id} - Get speaker details 