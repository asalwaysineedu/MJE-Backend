from dataclasses import dataclass
from enum import Enum


class LandingEventType(Enum):
    VIEW_LANDING = "view_landing"
    LANDING_TOP = "landing_top"
    LANDING_BOTTOM = "landing_bottom"

    @classmethod
    def allowed_values(cls) -> list[str]:
        return [e.value for e in cls]


@dataclass(frozen=True)
class LandingEvent:
    event_name: LandingEventType
    session_id: str
    timestamp: str
    page_path: str
