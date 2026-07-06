from dataclasses import dataclass
from typing import Optional

from app.domains.dwell_time.domain.events.dwell_time_event import DwellTimeEventType


@dataclass
class DwellTimeEntity:
    event_name: DwellTimeEventType
    session_id: str
    timestamp: str
    page_path: str
    device_type: str
    id: Optional[int] = None
