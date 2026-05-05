from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class RecommendationPlaceDto:
    order: int
    place_type: str
    id: int
    name: str
    category: str
    road_address: str
    address: str
    mapx: str
    mapy: str
    link: str
    telephone: str
    keyword: str
    collected_at: str
    duration_minutes: int
    image_url: Optional[str] = None


@dataclass
class RecommendationCourseItemDto:
    course_id: str
    grade: str
    places: List[RecommendationPlaceDto]
    image_url: Optional[str] = None


@dataclass
class GetRecommendationResponseDto:
    courses: List[RecommendationCourseItemDto]
    shortage_reasons: List[str] = field(default_factory=list)
