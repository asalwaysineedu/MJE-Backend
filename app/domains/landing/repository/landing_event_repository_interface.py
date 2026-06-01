from abc import ABC, abstractmethod

from app.domains.landing.domain.entity.landing_event_entity import LandingEventEntity


class LandingEventRepositoryInterface(ABC):
    @abstractmethod
    async def save(self, entity: LandingEventEntity) -> None: ...
