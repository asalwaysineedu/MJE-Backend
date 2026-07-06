from datetime import datetime

from pydantic import BaseModel, field_validator

from app.domains.dwell_time.domain.events.dwell_time_event import DwellTimeEventType
from app.domains.dwell_time.service.dto.request.record_dwell_time_event_request import (
    RecordDwellTimeEventRequest,
)


class DwellTimeRequestForm(BaseModel):
    session_id: str
    event_name: str
    timestamp: str
    page_path: str
    device_type: str

    @field_validator("event_name")
    @classmethod
    def validate_event_name(cls, v: str) -> str:
        allowed = DwellTimeEventType.allowed_values()
        if v not in allowed:
            raise ValueError(f"event_name must be one of {allowed}")
        return v

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, v: str) -> str:
        try:
            datetime.fromisoformat(v.replace("Z", "+00:00"))
        except ValueError:
            raise ValueError("timestamp must be an ISO 8601 datetime string, e.g. 2026-07-06T10:00:00Z")
        return v

    def to_request(self) -> RecordDwellTimeEventRequest:
        return RecordDwellTimeEventRequest(
            event_name=DwellTimeEventType(self.event_name),
            session_id=self.session_id,
            timestamp=self.timestamp,
            page_path=self.page_path,
            device_type=self.device_type,
        )
