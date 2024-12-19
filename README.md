# Hydropower Plant Exercise API

This project is an exercise API designed to provide CRUD operations for managing **Power Plants** and their associated **Weekly Productions**. The goal of this project is to practice data visualization, user experience (UX), user interface (UI), and creativity using real-world data structures.

## Overview

The API includes two core objects:

### **Power Plant**

- **Attributes**:
  - `id`: Unique identifier for the power plant.
  - `name`: Name of the power plant.
  - `location`: Location of the power plant.
  - `capacity_mw`: Maximum power capacity of the plant in megawatts (MW).
  - `status`: Current operational status. Possible values:
    - `Operational`
    - `Under Maintenance`
    - `Decommissioned`
  - `water_flow_rate`: Current water flow rate in cubic meters per second (m³/s).

### **Weekly Production**

- **Attributes**:
  - `id`: Unique identifier for the production entry.
  - `power_plant_id`: Reference to the associated power plant.
  - `production_date`: The date representing the start of the ISO week.
  - `production_mw`: Power produced during the week, in megawatts (MW).
  - `week_number`: The ISO week number derived from the `production_date`.
  - `year`: The ISO year derived from the `production_date`.

## Features

- Full CRUD operations for **Power Plants**.
- Full CRUD operations for **Weekly Productions**.
- Automatically generates weekly production data for each week within a specified range of years.
- Swagger documentation for easy API exploration.

## Installation Instructions

Follow these steps to set up the API locally:

> **Warning:** This project requires Python 3.11 or above.

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and Activate a Virtual Environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Setup Script**:

   ```bash
   python setup.py
   ```

   - **Warning**: The setup script will delete the existing database if one exists.
   - The script will:
     1. Delete the existing database (if any).
     2. Create a fresh database with the required tables.
     3. Populate the database with fixture data (20 power plants with weekly production data).

5. **Reinitialize the Database**:
   - To reset the database, simply rerun the setup script:
     ```bash
     python setup.py
     ```

## Running the API

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

### Accessing the API

Once the server is running, you can explore the API using Swagger UI:

- **Swagger Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Purpose

This project is intended to provide an environment for:

- Experimenting with front-end data visualization.
- Exploring user interface (UI) and user experience (UX) design.
- Practicing CRUD operations with real-world data structures.
- Developing creative solutions to represent and interact with hydropower plant data.

## Suggested Exercises

Here are some suggestions for exploring and building upon this API. None of these are mandatory; the idea is to present something, and these are just suggestions - combine approaches and explore creative solutions.

1. [FRONTEND] Build a front-end application to interact with the API:

- Create a table or list displaying all power plants and their associated data.
- Create interfaces to view, add, update, and delete power plants.
- Display weekly production data for selected power plants.
- Implement data visualizations to analyze production data:
  - Represent production data over time for a single plant or multiple plants.
  - Show trends over time for a single plant or multiple plants.
  - Compare production across plants or highlight anomalies.
- Build a comprehensive dashboard showing key metrics and trends.
- Introduce interactive visualizations and advanced analytics.
- Add export options to download reports or charts based on the data.

2. [BACKEND] Extend or modify the API functionality:

- Allow querying production data by date range or specific conditions.
- Add filtering and sorting capabilities for production data.
- Develop summary endpoints to calculate total and average production metrics.
- Enhance the API with additional endpoints for detailed analytics or anomaly detection.

## Suggested Libraries and Tools

| **Category**         | **Suggestions**              |
| -------------------- | ---------------------------- |
| Front-End Framework  | React, Next.js, MUI Toolpad  |
| UI Library           | Material-UI (MUI), Fluent UI |
| Data Visualization   | ECharts, Chart.js, D3.js     |
| Back-End Integration | Axios, Fetch API             |

## Notes for Users

- Users should create their project in a **separate repository** to interact with this API;
- Once completed, users are encouraged to submit their project for evaluation;
- If desired, users are welcome to **fork this repository** and implement their own customizations or changes to the API;
- Any combination of the suggested exercises and further exploration is encouraged to maximize learning;

Feel free to customize and extend this project as needed!

Have fun!
