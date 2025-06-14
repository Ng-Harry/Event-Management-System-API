from typing import List, Optional
from schemas.models import Speaker, SpeakerCreate

class SpeakerService:
    def __init__(self):
        self.speakers: List[Speaker] = []
        self._next_id = 1
        self._initialize_speakers()

    def _initialize_speakers(self):
        initial_speakers = [
            SpeakerCreate(name="John Doe", topic="Web Development"),
            SpeakerCreate(name="Jane Smith", topic="Data Science"),
            SpeakerCreate(name="Mike Johnson", topic="Cloud Computing")
        ]
        for speaker in initial_speakers:
            self.create_speaker(speaker)

    def create_speaker(self, speaker: SpeakerCreate) -> Speaker:
        new_speaker = Speaker(
            id=self._next_id,
            name=speaker.name,
            topic=speaker.topic
        )
        self.speakers.append(new_speaker)
        self._next_id += 1
        return new_speaker

    def get_speaker(self, speaker_id: int) -> Optional[Speaker]:
        return next((speaker for speaker in self.speakers if speaker.id == speaker_id), None)

    def get_all_speakers(self) -> List[Speaker]:
        return self.speakers

    def update_speaker(self, speaker_id: int, speaker_data: SpeakerCreate) -> Optional[Speaker]:
        speaker = self.get_speaker(speaker_id)
        if speaker:
            speaker.name = speaker_data.name
            speaker.topic = speaker_data.topic
        return speaker

    def delete_speaker(self, speaker_id: int) -> bool:
        speaker = self.get_speaker(speaker_id)
        if speaker:
            self.speakers.remove(speaker)
            return True
        return False 