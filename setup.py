import os
from faker import Faker
from sqlalchemy.orm import Session
from db import SessionLocal
from models.power_plants import PowerPlantDB
from models.weekly_production import WeeklyProductionDB
from datetime import datetime
import random

from db import Base, engine

from models import *  # noqa: F403 F401

DB_FILE_PATH = "./db.sqlite"
PLANTS_TO_CREATE = 20


def delete_existing_db(file_path: str = DB_FILE_PATH):
    """
    Delete the SQLite database file if it exists.
    """
    if os.path.exists(file_path):
        print(f"Deleting existing database at {file_path}...")
        os.remove(file_path)
        print("Database deleted successfully.")
    else:
        print(f"No existing database found at {file_path}.")


def init_db():
    """
    Ensures all tables are created in the database.
    """
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


def create_power_plants(db: Session, count: int = PLANTS_TO_CREATE):
    """
    Generate and insert fake power plant data into the database.
    """
    # Initialize Faker
    fake = Faker()
    power_plants = []
    for _ in range(count):
        plant = PowerPlantDB(
            name=fake.company(),
            location=fake.city(),
            capacity_mw=round(
                fake.random_number(digits=3, fix_len=True) / 10, 1
            ),
            status=fake.random_element(
                elements=("Operational", "Under Maintenance", "Decommissioned")
            ),
            water_flow_rate=round(
                fake.random_number(digits=3, fix_len=True) / 100, 2
            ),
        )
        db.add(plant)
        power_plants.append(plant)
    db.commit()
    return power_plants


def create_weekly_productions(
    db: Session,
    power_plants: list[PowerPlantDB],
    start_year=2020,
    end_year=2024,
):
    """
    Generate and insert weekly production data for each plant and each week of
    the given years.
    """
    for plant in power_plants:
        for year in range(start_year, end_year + 1):
            for week in range(1, 53):  # 52 weeks in a year
                try:
                    # Generate a production date for the start of the ISO week
                    production_date = datetime.strptime(
                        f"{year}-W{week}-1", "%G-W%V-%u"
                    )
                except ValueError:
                    # Handle the case of a 53rd week in non-ISO years
                    continue

                # Generate production between 10 MW and the plant's capacity
                production_mw = round(random.uniform(10, plant.capacity_mw), 1)

                # Create the weekly production entry
                weekly_production = WeeklyProductionDB(
                    power_plant_id=plant.id,
                    production_date=production_date,
                    production_mw=production_mw,
                )
                db.add(weekly_production)

    # Commit all generated weekly production records to the database
    db.commit()


def main():

    # Step 1: Delete existing database
    delete_existing_db()

    # Step 2: Initialize new database
    init_db()

    # Step 3: Populate the database
    db = SessionLocal()
    try:
        print("Creating power power_plants...")
        plants = create_power_plants(db)
        print("Power plants created successfully!")

        print("Creating weekly productions...")
        create_weekly_productions(db, plants)
        print("Weekly productions created successfully!")
    finally:
        db.close()


if __name__ == "__main__":
    main()
