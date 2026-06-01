from dataclasses import dataclass
from typing import Optional

from app.domains.landing.domain.events.landing_event import LandingEventType


@dataclass
class RecordLandingEventRequestDto:
    event_name: LandingEventType
    session_id: str
    timestamp: str
    page_path: str
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    referrer: Optional[str] = None
