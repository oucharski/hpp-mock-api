from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import (
    PowerPlantCreate,
    PowerPlantUpdate,
    PowerPlantListResponse,
    PowerPlantDetailResponse,
)
import controllers

router = APIRouter()


@router.get("/", response_model=list[PowerPlantListResponse])
def get_power_plants(db: Session = Depends(get_db)):
    return controllers.power_plants.all(db)


@router.post("/", response_model=PowerPlantListResponse)
def create_power_plant(plant: PowerPlantCreate, db: Session = Depends(get_db)):
    return controllers.power_plants.create(db, plant)


@router.get("/{power_plant_id}", response_model=PowerPlantDetailResponse)
def get_power_plant(power_plant_id: int, db: Session = Depends(get_db)):
    return controllers.power_plants.by_id(db, power_plant_id)


@router.put("/{power_plant_id}", response_model=PowerPlantListResponse)
def update_power_plant(
    power_plant_id: int,
    power_plant: PowerPlantUpdate,
    db: Session = Depends(get_db),
):
    return controllers.power_plants.update(db, power_plant_id, power_plant)


@router.delete("/{plant_id}")
def delete_plant(power_plant_id: int, db: Session = Depends(get_db)):
    controllers.power_plants.destroy(db, power_plant_id)
    return {"message": "Plant deleted successfully"}
