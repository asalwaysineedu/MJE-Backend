from app.domains.landing.domain.entity.landing_event_entity import LandingEventEntity
from app.domains.landing.domain.events.landing_event import LandingEventType
from app.domains.landing.repository.orm.landing_event_orm import LandingEventOrm


def to_orm(entity: LandingEventEntity) -> LandingEventOrm:
    return LandingEventOrm(
        event_name=entity.event_name.value,
        session_id=entity.session_id,
        timestamp=entity.timestamp,
        page_path=entity.page_path,
        utm_source=entity.utm_source,
        utm_medium=entity.utm_medium,
        referrer=entity.referrer,
    )


def to_entity(orm: LandingEventOrm) -> LandingEventEntity:
    return LandingEventEntity(
        id=orm.id,
        event_name=LandingEventType(orm.event_name),
        session_id=orm.session_id,
        timestamp=orm.timestamp,
        page_path=orm.page_path,
        utm_source=orm.utm_source,
        utm_medium=orm.utm_medium,
        referrer=orm.referrer,
    )
