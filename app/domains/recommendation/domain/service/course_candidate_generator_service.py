from itertools import product
from typing import List, Set, Tuple

from app.domains.recommendation.domain.entity.course_candidate import CourseCandidate
from app.domains.recommendation.domain.value_object.activity_type import ActivityKind
from app.domains.recommendation.domain.value_object.candidate_place import CandidatePlace

MIN_CANDIDATES = 10

_NIGHTLIFE_KINDS: Set[ActivityKind] = {
    ActivityKind.BAR,
    ActivityKind.KARAOKE,
    ActivityKind.LATE_NIGHT,
    ActivityKind.NIGHT_VIEW,
}


class CourseCandidateGeneratorService:
    def generate(
        self,
        restaurant_candidates: List[CandidatePlace],
        cafe_candidates: List[CandidatePlace],
        activity_candidates: List[CandidatePlace],
    ) -> Tuple[List[CourseCandidate], List[str]]:
        shortage_reasons = self._check_input_shortages(
            restaurant_candidates, cafe_candidates, activity_candidates
        )

        nightlife = [a for a in activity_candidates if a.activity_kind in _NIGHTLIFE_KINDS]
        core = [a for a in activity_candidates if a.activity_kind and a.activity_kind.is_core]

        candidates: List[CourseCandidate] = []

        # 식당 + 카페 + 활동
        for r, c, a in product(restaurant_candidates, cafe_candidates, activity_candidates):
            if not self._has_duplicate(r, c, a):
                candidates.append(CourseCandidate(restaurant=r, second=c, third=a))

        # 식당 + 나이트라이프 + 코어활동 (카페 없음)
        for r, n, c in product(restaurant_candidates, nightlife, core):
            if not self._has_duplicate(r, n, c):
                candidates.append(CourseCandidate(restaurant=r, second=n, third=c))

        # 식당 + 나이트라이프1 + 나이트라이프2 (다른 종류, 카페 없음)
        for r, n1, n2 in product(restaurant_candidates, nightlife, nightlife):
            if n1.activity_kind != n2.activity_kind and not self._has_duplicate(r, n1, n2):
                candidates.append(CourseCandidate(restaurant=r, second=n1, third=n2))

        if len(candidates) < MIN_CANDIDATES:
            shortage_reasons.append(
                f"코스 후보가 {MIN_CANDIDATES}개 미만입니다 (현재 {len(candidates)}개)"
            )

        return candidates, shortage_reasons

    def _has_duplicate(self, *places: CandidatePlace) -> bool:
        ids = [p.id for p in places]
        if len(ids) != len(set(ids)):
            return True
        name_addresses = [(p.name, p.address) for p in places]
        return len(name_addresses) != len(set(name_addresses))

    def _check_input_shortages(
        self,
        restaurants: List[CandidatePlace],
        cafes: List[CandidatePlace],
        activities: List[CandidatePlace],
    ) -> List[str]:
        reasons = []
        if not restaurants:
            reasons.append("레스토랑 후보가 없습니다")
        if not cafes:
            reasons.append("카페 후보가 없습니다")
        if not activities:
            reasons.append("액티비티 후보가 없습니다")
        return reasons
