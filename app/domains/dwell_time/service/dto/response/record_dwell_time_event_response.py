from dataclasses import dataclass
from typing import Optional


@dataclass
class RecordDwellTimeEventResponse:
    success: bool
    duration_ms: Optional[int] = None
