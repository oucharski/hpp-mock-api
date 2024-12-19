from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Define the database URL (SQLite in this case)
DATABASE_URL = "sqlite:///./db.sqlite"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Define the base class for models
Base = declarative_base()

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency for FastAPI to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
