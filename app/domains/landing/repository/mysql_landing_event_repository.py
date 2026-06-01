from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.landing.domain.entity.landing_event_entity import LandingEventEntity
from app.domains.landing.repository.landing_event_repository_interface import LandingEventRepositoryInterface
from app.domains.landing.repository.mapper.landing_event_mapper import to_orm


class MysqlLandingEventRepository(LandingEventRepositoryInterface):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save(self, entity: LandingEventEntity) -> None:
        orm = to_orm(entity)
        self._session.add(orm)
        await self._session.flush()
