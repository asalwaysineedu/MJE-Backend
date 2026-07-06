from app.domains.dwell_time.domain.entity.dwell_time_entity import DwellTimeEntity
from app.domains.dwell_time.domain.events.dwell_time_event import DwellTimeEventType
from app.domains.dwell_time.domain.service.dwell_time_calculator import DwellTimeCalculator
from app.domains.dwell_time.repository.dwell_time_repository_interface import DwellTimeRepositoryInterface
from app.domains.dwell_time.service.dto.request.record_dwell_time_event_request import (
    RecordDwellTimeEventRequest,
)
from app.domains.dwell_time.service.dto.response.record_dwell_time_event_response import (
    RecordDwellTimeEventResponse,
)


class RecordDwellTimeEventUseCase:
    def __init__(self, repository: DwellTimeRepositoryInterface) -> None:
        self._repository = repository

    async def execute(self, dto: RecordDwellTimeEventRequest) -> RecordDwellTimeEventResponse:
        entity = DwellTimeEntity(
            event_name=dto.event_name,
            session_id=dto.session_id,
            timestamp=dto.timestamp,
            page_path=dto.page_path,
            device_type=dto.device_type,
        )
        await self._repository.save(entity)

        duration_ms = None
        if dto.event_name == DwellTimeEventType.PAGE_LEAVE:
            events = await self._repository.find_by_session_id(dto.session_id)
            duration_ms = DwellTimeCalculator.calculate_active_duration_ms(events)

        return RecordDwellTimeEventResponse(success=True, duration_ms=duration_ms)
