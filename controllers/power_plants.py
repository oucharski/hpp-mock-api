from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.power_plants import (
    PowerPlantDB,
    PowerPlantCreate,
    PowerPlantUpdate,
)


def by_id(db: Session, power_plant_id: int):
    return (
        db.query(PowerPlantDB)
        .filter(PowerPlantDB.id == power_plant_id)
        .first()
    )


def all(db: Session):
    return db.query(PowerPlantDB).all()


def create(db: Session, plant: PowerPlantCreate):
    db_plant = PowerPlantDB(**plant.dict())
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant


def update(db: Session, power_plant_id: int, plant: PowerPlantUpdate):
    db_plant = (
        db.query(PowerPlantDB)
        .filter(PowerPlantDB.id == power_plant_id)
        .first()
    )
    if not db_plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    for key, value in plant.dict(exclude_unset=True).items():
        setattr(db_plant, key, value)
    db.commit()
    db.refresh(db_plant)
    return db_plant


def destroy(db: Session, power_plant_id: int):
    db_plant = (
        db.query(PowerPlantDB)
        .filter(PowerPlantDB.id == power_plant_id)
        .first()
    )
    if not db_plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    db.delete(db_plant)
    db.commit()
