from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.dwell_time.domain.entity.dwell_time_entity import DwellTimeEntity
from app.domains.dwell_time.repository.dwell_time_repository_interface import DwellTimeRepositoryInterface
from app.domains.dwell_time.repository.mapper.dwell_time_mapper import to_entity, to_orm
from app.domains.dwell_time.repository.orm.dwell_time_orm import DwellTimeOrm


class MysqlDwellTimeRepository(DwellTimeRepositoryInterface):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save(self, entity: DwellTimeEntity) -> None:
        orm = to_orm(entity)
        self._session.add(orm)
        await self._session.flush()

    async def find_by_session_id(self, session_id: str) -> list[DwellTimeEntity]:
        result = await self._session.execute(
            select(DwellTimeOrm)
            .where(DwellTimeOrm.session_id == session_id)
            .order_by(DwellTimeOrm.timestamp)
        )
        return [to_entity(orm) for orm in result.scalars().all()]
