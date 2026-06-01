from dataclasses import dataclass
from typing import Optional

from app.domains.landing.domain.events.landing_event import LandingEventType


@dataclass
class LandingEventEntity:
    event_name: LandingEventType
    session_id: str
    timestamp: str
    page_path: str
    id: Optional[int] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    referrer: Optional[str] = None
