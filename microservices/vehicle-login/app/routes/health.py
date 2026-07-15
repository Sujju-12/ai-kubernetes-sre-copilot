from fastapi import APIRouter
from sqlalchemy import text

from app.database import engine

router = APIRouter(tags=["Health"])


@router.get("/live")
def live():
    """
    Liveness Probe
    Used by Kubernetes to verify
    the application process is alive.
    """

    return {
        "status": "alive"
    }


@router.get("/ready")
def ready():
    """
    Readiness Probe

    Checks whether the application
    can communicate with PostgreSQL.
    """

    try:

        with engine.connect() as connection:

            connection.execute(text("SELECT 1"))

        return {
            "status": "ready",
            "database": "connected"
        }

    except Exception as e:

        return {
            "status": "not ready",
            "database": str(e)
        }
