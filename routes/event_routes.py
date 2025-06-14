from fastapi import APIRouter, HTTPException
from typing import List
from schemas.models import Event, EventCreate
from services.event_service import EventService

router = APIRouter(prefix="/events", tags=["events"])
event_service = EventService()

@router.post("/", response_model=Event)
def create_event(event: EventCreate):
    return event_service.create_event(event)

@router.get("/", response_model=List[Event])
def get_events():
    return event_service.get_all_events()

@router.get("/{event_id}", response_model=Event)
def get_event(event_id: int):
    event = event_service.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=Event)
def update_event(event_id: int, event: EventCreate):
    updated_event = event_service.update_event(event_id, event)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.delete("/{event_id}")
def delete_event(event_id: int):
    if not event_service.delete_event(event_id):
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}

@router.patch("/{event_id}/close", response_model=Event)
def close_event(event_id: int):
    event = event_service.close_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event 