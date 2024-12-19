from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import plants_router, production_router

app = FastAPI(
    title="Hydropower Plant Mock API",
    description="API for managing and monitoring hydropower power_plants.",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers with prefixes
app.include_router(plants_router, prefix="/plants", tags=["Plants"])
app.include_router(production_router, prefix="/production", tags=["Production"])
