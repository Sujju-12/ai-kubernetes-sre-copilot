from fastapi import APIRouter

router = APIRouter(tags=["Authentication"])


@router.get("/")
def home():
    return {
        "message": "Vehicle Login API Running"
    }


@router.post("/login")
def login():
    return {
        "status": "success",
        "token": "dummy-jwt-token"
    }
