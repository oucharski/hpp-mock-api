from .power_plants import (
    PowerPlantDB,
    PowerPlantCreate,
    PowerPlantUpdate,
    PowerPlantListResponse,
    PowerPlantDetailResponse,
    PowerPlantBase,
)
from .weekly_production import (
    WeeklyProductionDB,
    WeeklyProductionCreate,
    WeeklyProductionResponse,
    WeeklyProductionBase,
)

# Export all models for easy access
__all__ = [
    "PowerPlantDB",
    "PowerPlantCreate",
    "PowerPlantUpdate",
    "PowerPlantListResponse",
    "PowerPlantDetailResponse",
    "PowerPlantBase",
    "WeeklyProductionDB",
    "WeeklyProductionCreate",
    "WeeklyProductionResponse",
    "WeeklyProductionBase",
]
