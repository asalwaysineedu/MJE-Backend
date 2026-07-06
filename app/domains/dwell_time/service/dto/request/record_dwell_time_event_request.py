from dataclasses import dataclass

from app.domains.dwell_time.domain.events.dwell_time_event import DwellTimeEventType


@dataclass
class RecordDwellTimeEventRequest:
    event_name: DwellTimeEventType
    session_id: str
    timestamp: str
    page_path: str
    device_type: str
