import os

APP_NAME = os.getenv("APP_NAME", "Vehicle Login Service")
APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
DATABASE_NAME = os.getenv("DATABASE_NAME", "vehicle_db")

DATABASE_USER = os.getenv("DATABASE_USER", "vehicle_admin")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "Vehicle@123")
