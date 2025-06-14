from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        from_attributes = True

class EventBase(BaseModel):
    title: str
    location: str
    date: datetime

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    is_open: bool = True

    class Config:
        from_attributes = True

class SpeakerBase(BaseModel):
    name: str
    topic: str

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase):
    id: int

    class Config:
        from_attributes = True

class RegistrationBase(BaseModel):
    user_id: int
    event_id: int

class RegistrationCreate(RegistrationBase):
    pass

class Registration(RegistrationBase):
    id: int
    registration_date: datetime
    attended: bool = False

    class Config:
        from_attributes = True 