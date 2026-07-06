from app.domains.dwell_time.domain.entity.dwell_time_entity import DwellTimeEntity
from app.domains.dwell_time.domain.events.dwell_time_event import DwellTimeEventType
from app.domains.dwell_time.repository.orm.dwell_time_orm import DwellTimeOrm


def to_orm(entity: DwellTimeEntity) -> DwellTimeOrm:
    return DwellTimeOrm(
        session_id=entity.session_id,
        event_name=entity.event_name.value,
        timestamp=entity.timestamp,
        page_path=entity.page_path,
        device_type=entity.device_type,
    )


def to_entity(orm: DwellTimeOrm) -> DwellTimeEntity:
    return DwellTimeEntity(
        id=orm.id,
        event_name=DwellTimeEventType(orm.event_name),
        session_id=orm.session_id,
        timestamp=orm.timestamp,
        page_path=orm.page_path,
        device_type=orm.device_type,
    )
