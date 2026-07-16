from pydantic import BaseModel


class DiagnoseRequest(BaseModel):
    namespace: str


class HealthResponse(BaseModel):
    status: str
