from app.domains.landing.domain.entity.landing_event_entity import LandingEventEntity
from app.domains.landing.repository.landing_event_repository_interface import LandingEventRepositoryInterface
from app.domains.landing.service.dto.request.record_landing_event_request_dto import RecordLandingEventRequestDto
from app.domains.landing.service.dto.response.record_landing_event_response_dto import RecordLandingEventResponseDto


class RecordLandingEventUseCase:
    def __init__(self, repository: LandingEventRepositoryInterface) -> None:
        self._repository = repository

    async def execute(self, dto: RecordLandingEventRequestDto) -> RecordLandingEventResponseDto:
        entity = LandingEventEntity(
            event_name=dto.event_name,
            session_id=dto.session_id,
            timestamp=dto.timestamp,
            page_path=dto.page_path,
            utm_source=dto.utm_source,
            utm_medium=dto.utm_medium,
            referrer=dto.referrer,
        )
        await self._repository.save(entity)
        return RecordLandingEventResponseDto(success=True)
