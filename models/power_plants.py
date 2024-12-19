from pydantic import BaseModel
from typing import Literal
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base
from models.weekly_production import WeeklyProductionResponse


class PowerPlantDB(Base):
    __tablename__ = "power_plants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    capacity_mw = Column(Float)
    status = Column(String)
    water_flow_rate = Column(Float)

    # Relationship to WeeklyProductionDB
    weekly_production = relationship(
        "WeeklyProductionDB", back_populates="power_plant"
    )


class PowerPlantBase(BaseModel):
    name: str
    location: str
    capacity_mw: float
    status: Literal["Operational", "Under Maintenance", "Decommissioned"]
    water_flow_rate: float


class PowerPlantCreate(PowerPlantBase):
    pass


class PowerPlantUpdate(BaseModel):
    name: str | None = None
    location: str | None = None
    capacity_mw: float | None = None
    status: (
        Literal["Operational", "Under Maintenance", "Decommissioned"] | None
    ) = None
    water_flow_rate: float | None = None


class PowerPlantListResponse(PowerPlantBase):
    id: int

    class Config:
        from_attributes = True


class PowerPlantDetailResponse(PowerPlantBase):
    id: int
    weekly_production: list[WeeklyProductionResponse] = []

    class Config:
        from_attributes = True
