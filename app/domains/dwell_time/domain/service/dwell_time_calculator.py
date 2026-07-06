from datetime import datetime
from typing import Optional

from app.domains.dwell_time.domain.entity.dwell_time_entity import DwellTimeEntity
from app.domains.dwell_time.domain.events.dwell_time_event import DwellTimeEventType

_RESUME_EVENTS = (DwellTimeEventType.PAGE_ENTER, DwellTimeEventType.PAGE_VISIBLE)
_PAUSE_EVENTS = (DwellTimeEventType.PAGE_HIDDEN, DwellTimeEventType.PAGE_LEAVE)


class DwellTimeCalculator:
    """page_enter/page_visible(재개) ~ page_hidden/page_leave(중단) 구간들의 합으로 실제 체류 시간을 구한다."""

    @staticmethod
    def calculate_active_duration_ms(events: list[DwellTimeEntity]) -> int:
        if not events:
            return 0

        sorted_events = sorted(events, key=lambda e: DwellTimeCalculator._parse(e.timestamp))

        active_seconds = 0.0
        segment_start: Optional[datetime] = None

        for event in sorted_events:
            ts = DwellTimeCalculator._parse(event.timestamp)
            if event.event_name in _RESUME_EVENTS:
                if segment_start is None:
                    segment_start = ts
            elif event.event_name in _PAUSE_EVENTS:
                if segment_start is not None:
                    active_seconds += (ts - segment_start).total_seconds()
                    segment_start = None

        return int(max(active_seconds, 0.0) * 1000)

    @staticmethod
    def _parse(timestamp: str) -> datetime:
        return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
