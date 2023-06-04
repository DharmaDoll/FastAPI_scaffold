from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.routers.auth import get_current_active_user
from api.db import get_db


# from common.models import User
import api.models.task as task_model
import api.schemas.user as user_schema
import api.cruds.user as user_crud


router = APIRouter()


@router.get("/users/me", response_model=user_schema.User)
async def read_users_me(current_user: task_model.User = Depends(get_current_active_user)):
    return current_user


@router.post("/users", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = user_crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return user_crud.create_user(db=db, user=user)