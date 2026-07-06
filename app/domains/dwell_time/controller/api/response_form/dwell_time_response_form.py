from typing import Optional

from pydantic import BaseModel

from app.domains.dwell_time.service.dto.response.record_dwell_time_event_response import (
    RecordDwellTimeEventResponse,
)


class DwellTimeResponseForm(BaseModel):
    success: bool
    duration_ms: Optional[int] = None

    @classmethod
    def from_response(cls, dto: RecordDwellTimeEventResponse) -> "DwellTimeResponseForm":
        return cls(success=dto.success, duration_ms=dto.duration_ms)
