from fastapi import APIRouter

from app.config import APP_VERSION

router = APIRouter(tags=["Version"])


@router.get("/version")
def version():

    return {
        "version": APP_VERSION
    }
