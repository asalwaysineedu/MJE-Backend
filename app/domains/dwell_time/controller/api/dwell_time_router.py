from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.dwell_time.controller.api.request_form.dwell_time_request_form import DwellTimeRequestForm
from app.domains.dwell_time.controller.api.response_form.dwell_time_response_form import DwellTimeResponseForm
from app.domains.dwell_time.repository.mysql_dwell_time_repository import MysqlDwellTimeRepository
from app.domains.dwell_time.service.usecase.record_dwell_time_event_usecase import RecordDwellTimeEventUseCase
from app.infrastructure.database.database import get_db

router = APIRouter(prefix="/dwell_time", tags=["dwell_time"])


@router.post("/session/events", response_model=DwellTimeResponseForm, status_code=200)
async def record_dwell_time_event(
    form: DwellTimeRequestForm,
    db: AsyncSession = Depends(get_db),
) -> DwellTimeResponseForm:
    repository = MysqlDwellTimeRepository(db)
    usecase = RecordDwellTimeEventUseCase(repository)
    dto = await usecase.execute(form.to_request())
    return DwellTimeResponseForm.from_response(dto)
