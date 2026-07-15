from fastapi import FastAPI

from app.routes.login import router as login_router
from app.routes.health import router as health_router
from app.routes.version import router as version_router


app = FastAPI(
    title="Vehicle Login Service",
    version="1.0.1",
    description="Vehicle Login Microservice"
)

app.include_router(login_router)
app.include_router(health_router)
app.include_router(version_router)
