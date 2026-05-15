from dataclasses import dataclass
from typing import Optional

from app.domains.home.domain.events.home_event import HomeEventType


@dataclass
class RecordHomeEventRequestDto:
    event_name: HomeEventType
    session_id: str
    timestamp: str
    page_path: str
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    referrer: Optional[str] = None
