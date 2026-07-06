from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.infrastructure.database.database import Base


class DwellTimeOrm(Base):
    __tablename__ = "dwell_time_events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(255), nullable=False, index=True)
    event_name = Column(String(50), nullable=False)
    timestamp = Column(String(50), nullable=False)
    page_path = Column(String(500), nullable=False)
    device_type = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now(), nullable=False)
