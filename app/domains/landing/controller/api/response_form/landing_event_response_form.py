from pydantic import BaseModel

from app.domains.landing.service.dto.response.record_landing_event_response_dto import RecordLandingEventResponseDto


class LandingEventResponseForm(BaseModel):
    success: bool

    @classmethod
    def from_response(cls, dto: RecordLandingEventResponseDto) -> "LandingEventResponseForm":
        return cls(success=dto.success)
