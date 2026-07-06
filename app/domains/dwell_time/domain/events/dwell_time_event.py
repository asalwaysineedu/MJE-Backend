from enum import Enum


class DwellTimeEventType(Enum):
    PAGE_ENTER = "page_enter"
    PAGE_LEAVE = "page_leave"
    PAGE_HIDDEN = "page_hidden"
    PAGE_VISIBLE = "page_visible"
    HEARTBEAT = "heartbeat"

    @classmethod
    def allowed_values(cls) -> list[str]:
        return [e.value for e in cls]