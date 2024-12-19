from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db import get_db
from models import WeeklyProductionCreate, WeeklyProductionResponse
import controllers

router = APIRouter()


@router.post(
    "/{power_plant_id}/weekly-productions",
    response_model=WeeklyProductionResponse,
)
def add_weekly_production(
    power_plant_id: int,
    production: WeeklyProductionCreate,
    db: Session = Depends(get_db),
):
    try:
        return controllers.weekly_production.create(
            db, power_plant_id, production
        )
    except ValueError as e:
        if "Plant not found" in str(e):
            raise HTTPException(
                status_code=404, detail=str(e)
            )  # Specific 404 error
        raise HTTPException(
            status_code=400, detail=str(e)
        )  # Generic 400 error


@router.get(
    "/{power_plant_id}/weekly-productions",
    response_model=list[WeeklyProductionResponse],
)
def get_weekly_productions(power_plant_id: int, db: Session = Depends(get_db)):
    plant = controllers.power_plants.by_id(db, power_plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    return controllers.weekly_production.get_by_power_plant_id(
        db, power_plant_id
    )


@router.delete("/weekly-productions/{production_id}")
def delete_weekly_production(
    production_id: int, db: Session = Depends(get_db)
):
    controllers.weekly_production.destroy(db, production_id)
    return {"message": "Weekly production record deleted successfully"}


@router.get(
    "/{power_plant_id}/weekly-productions/time-range",
    response_model=list[WeeklyProductionResponse],
)
def get_weekly_productions_by_time_range(
    power_plant_id: int,
    start_date: datetime = Query(..., description="Start date in ISO format"),
    end_date: datetime = Query(..., description="End date in ISO format"),
    db: Session = Depends(get_db),
):
    # Validate plant existence
    plant = controllers.powerpower_plants.by_id(db, power_plant_id)
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")

    # Fetch records within the time range
    try:
        return controllers.weekly_production.get_by_time_range(
            db, power_plant_id, start_date, end_date
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
