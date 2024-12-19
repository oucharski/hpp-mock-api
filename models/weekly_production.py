from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class WeeklyProductionDB(Base):
    __tablename__ = "weekly_productions"
    id = Column(Integer, primary_key=True, index=True)
    power_plant_id = Column(
        Integer, ForeignKey("power_plants.id"), nullable=False
    )
    production_date = Column(DateTime, nullable=False)
    production_mw = Column(Float, nullable=False)
    power_plant = relationship(
        "PowerPlantDB", back_populates="weekly_production"
    )

    @property
    def week_number(self):
        """
        Get the ISO week number from the production date.
        """
        return self.production_date.isocalendar()[1]

    @property
    def year(self):
        """
        Get the ISO year from the production date.
        """
        return self.production_date.isocalendar()[0]


# Pydantic Models
class WeeklyProductionBase(BaseModel):
    week_number: int
    production_mw: float


class WeeklyProductionCreate(BaseModel):
    production_date: datetime
    production_mw: float


class WeeklyProductionResponse(BaseModel):
    id: int
    power_plant_id: int
    week_number: int
    year: int
    production_mw: float
    production_date: datetime

    class Config:
        from_attributes = True
