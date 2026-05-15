from app.domains.home.domain.entity.home_event_entity import HomeEventEntity
from app.domains.home.repository.home_event_repository_interface import HomeEventRepositoryInterface
from app.domains.home.service.dto.request.record_home_event_request_dto import RecordHomeEventRequestDto
from app.domains.home.service.dto.response.record_home_event_response_dto import RecordHomeEventResponseDto


class RecordHomeEventUseCase:
    def __init__(self, repository: HomeEventRepositoryInterface) -> None:
        self._repository = repository

    async def execute(self, dto: RecordHomeEventRequestDto) -> RecordHomeEventResponseDto:
        entity = HomeEventEntity(
            event_name=dto.event_name,
            session_id=dto.session_id,
            timestamp=dto.timestamp,
            page_path=dto.page_path,
            utm_source=dto.utm_source,
            utm_medium=dto.utm_medium,
            referrer=dto.referrer,
        )
        await self._repository.save(entity)
        return RecordHomeEventResponseDto(success=True)
