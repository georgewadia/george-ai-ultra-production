from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from jose import jwt

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

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

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )