from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.landing.controller.api.request_form.landing_event_request_form import LandingEventRequestForm
from app.domains.landing.controller.api.response_form.landing_event_response_form import LandingEventResponseForm
from app.domains.landing.repository.mysql_landing_event_repository import MysqlLandingEventRepository
from app.domains.landing.service.usecase.record_landing_event_usecase import RecordLandingEventUseCase
from app.infrastructure.database.database import get_db

router = APIRouter(prefix="/landing", tags=["landing"])


@router.post("/events", response_model=LandingEventResponseForm, status_code=200)
async def record_landing_event(
    form: LandingEventRequestForm,
    db: AsyncSession = Depends(get_db),
) -> LandingEventResponseForm:
    repository = MysqlLandingEventRepository(db)
    usecase = RecordLandingEventUseCase(repository)
    dto = await usecase.execute(form.to_request())
    return LandingEventResponseForm.from_response(dto)
