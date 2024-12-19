from datetime import datetime
from sqlalchemy.orm import Session
from models import WeeklyProductionDB, WeeklyProductionCreate, PowerPlantDB


def create(
    db: Session, power_plant_id: int, production: WeeklyProductionCreate
):
    # Check if the plant exists
    plant = (
        db.query(PowerPlantDB)
        .filter(PowerPlantDB.id == power_plant_id)
        .first()
    )
    if not plant:
        raise ValueError("Plant not found")

    # Extract week number and year from production_date
    week_number = production.production_date.isocalendar()[1]
    year = production.production_date.year

    # Create the new production instance
    new_production = WeeklyProductionDB(
        power_plant_id=power_plant_id,
        production_date=production.production_date,
        production_mw=production.production_mw,
    )
    db.add(new_production)
    db.commit()
    db.refresh(new_production)

    # Return the new production record with week_number and year
    return {
        "id": new_production.id,
        "power_plant_id": power_plant_id,
        "week_number": week_number,
        "year": year,
        "production_mw": new_production.production_mw,
    }


def destroy(db: Session, production_id: int):
    production = (
        db.query(WeeklyProductionDB)
        .filter(WeeklyProductionDB.id == production_id)
        .first()
    )
    if not production:
        return None
    db.delete(production)
    db.commit()


def get_by_power_plant_id(db: Session, power_plant_id: int):
    return (
        db.query(WeeklyProductionDB)
        .filter(WeeklyProductionDB.power_plant_id == power_plant_id)
        .order_by(
            WeeklyProductionDB.production_date.asc()
        )  # Sort by production_date
        .all()
    )


def get_by_time_range(
    db: Session, power_plant_id: int, start_date: datetime, end_date: datetime
):
    return (
        db.query(WeeklyProductionDB)
        .filter(
            WeeklyProductionDB.power_plant_id == power_plant_id,
            WeeklyProductionDB.production_date >= start_date,
            WeeklyProductionDB.production_date <= end_date,
        )
        .all()
    )
