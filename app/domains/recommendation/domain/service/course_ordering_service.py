from dataclasses import dataclass
from typing import List, Set

from app.domains.recommendation.domain.entity.course_candidate import CourseCandidate
from app.domains.recommendation.domain.service.duration_calculator_service import (
    DurationCalculatorService,
    DurationResult,
)
from app.domains.recommendation.domain.value_object.activity_type import ActivityKind
from app.domains.recommendation.domain.value_object.candidate_place import CandidatePlace
from app.domains.recommendation.domain.value_object.ordered_place import OrderedPlace
from app.domains.recommendation.domain.value_object.place_type import PlaceType
from app.domains.recommendation.domain.value_object.time_slot import TimeSlot
from app.domains.recommendation.domain.value_object.transport import Transport

# 점심: 식당 → 카페 → 활동 / 오후: 카페 → 활동 → 식당 / 저녁·밤: 식당 → 활동 → 카페
_CAFE_VISIT_ORDER = {
    TimeSlot.LUNCH:     [PlaceType.RESTAURANT, PlaceType.CAFE, PlaceType.ACTIVITY],
    TimeSlot.AFTERNOON: [PlaceType.CAFE, PlaceType.ACTIVITY, PlaceType.RESTAURANT],
    TimeSlot.EVENING:   [PlaceType.RESTAURANT, PlaceType.ACTIVITY, PlaceType.CAFE],
    TimeSlot.NIGHT:     [PlaceType.RESTAURANT, PlaceType.ACTIVITY, PlaceType.CAFE],
}

_NIGHTLIFE_LAST_KINDS: Set[ActivityKind] = {
    ActivityKind.BAR,
    ActivityKind.KARAOKE,
    ActivityKind.LATE_NIGHT,
    ActivityKind.NIGHT_VIEW,
}


@dataclass
class OrderedCourseResult:
    places: List[OrderedPlace]
    total_duration_minutes: int
    duration_score: float
    is_valid: bool


class CourseOrderingService:
    def __init__(self) -> None:
        self._duration_calculator = DurationCalculatorService()

    def apply_order(
        self,
        candidate: CourseCandidate,
        start_time: str,
        transport: Transport,
    ) -> OrderedCourseResult:
        ordered_places = self._determine_order(candidate, TimeSlot.from_start_time(start_time))

        duration_result: DurationResult = self._duration_calculator.calculate_for_places(
            ordered_places, start_time, transport
        )

        places = [
            OrderedPlace(
                order=i + 1,
                place=ordered_places[i],
                schedule=duration_result.place_schedules[i],
            )
            for i in range(len(ordered_places))
        ]

        return OrderedCourseResult(
            places=places,
            total_duration_minutes=duration_result.total_duration_minutes,
            duration_score=duration_result.duration_score,
            is_valid=duration_result.is_valid,
        )

    def _determine_order(
        self, candidate: CourseCandidate, time_slot: TimeSlot
    ) -> List[CandidatePlace]:
        second, third = candidate.second, candidate.third

        if second.place_type == PlaceType.CAFE:
            # Type A: restaurant + cafe + activity
            # 나이트라이프 활동은 항상 마지막
            third_kind = third.activity_kind
            if third_kind in _NIGHTLIFE_LAST_KINDS:
                order = [PlaceType.RESTAURANT, PlaceType.CAFE, PlaceType.ACTIVITY]
            else:
                order = _CAFE_VISIT_ORDER[time_slot]
            place_map = {
                PlaceType.RESTAURANT: candidate.restaurant,
                PlaceType.CAFE: second,
                PlaceType.ACTIVITY: third,
            }
            return [place_map[pt] for pt in order]

        # Type B/C: restaurant + activity + activity
        # 나이트라이프가 있으면 마지막에 배치
        second_is_nightlife = (second.activity_kind in _NIGHTLIFE_LAST_KINDS) if second.activity_kind else False
        if second_is_nightlife:
            return [candidate.restaurant, third, second]
        return [candidate.restaurant, second, third]
