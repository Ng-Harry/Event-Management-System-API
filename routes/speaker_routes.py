from fastapi import APIRouter, HTTPException
from typing import List
from schemas.models import Speaker
from services.speaker_service import SpeakerService

router = APIRouter(prefix="/speakers", tags=["speakers"])
speaker_service = SpeakerService()

@router.get("/", response_model=List[Speaker])
def get_speakers():
    return speaker_service.get_all_speakers()

@router.get("/{speaker_id}", response_model=Speaker)
def get_speaker(speaker_id: int):
    speaker = speaker_service.get_speaker(speaker_id)
    if not speaker:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return speaker 