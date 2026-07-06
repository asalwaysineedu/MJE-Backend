from abc import ABC, abstractmethod

from app.domains.dwell_time.domain.entity.dwell_time_entity import DwellTimeEntity


class DwellTimeRepositoryInterface(ABC):
    @abstractmethod
    async def save(self, entity: DwellTimeEntity) -> None: ...

    @abstractmethod
    async def find_by_session_id(self, session_id: str) -> list[DwellTimeEntity]: ...
