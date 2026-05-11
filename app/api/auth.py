from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from jose import jwt

router = APIRouter()

SECRET_KEY = "GEORGE_AI_SECRET"

ALGORITHM = "HS256"


class LoginData(BaseModel):

    username: str
    password: str


@router.post("/auth/login")
async def login(data: LoginData):

    # بيانات الأدمن
    if (
        data.username != "admin"
        or data.password != "123456"
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    expire = datetime.utcnow() + timedelta(days=1)

    token = jwt.encode(
        {
            "sub": data.username,
            "exp": expire
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token
    }