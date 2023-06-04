# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


# from common import models, schemas
import api.models.task as task_model
import api.schemas.user as user_schema
from api.security import get_password_hash


# from typing import List, Tuple, Optional
# from sqlalchemy.engine import Result
# from sqlalchemy import select


def get_user(db: AsyncSession, user_id: str):
    return db.query(task_model.User).filter(task_model.User.id == user_id).first()


def get_user_by_email(db: AsyncSession, email: str):
    return db.query(task_model.User).filter(task_model.User.email == email).first()


def get_user_by_username(db: AsyncSession, username: str):
    return db.query(task_model.User).filter(task_model.User.username == username).first()


def get_users(db: AsyncSession, skip: get_user = 0, limit: get_user = 100):
    return db.query(task_model.User).offset(skip).limit(limit).all()


def create_user(db: AsyncSession, user: user_schema.UserCreate):
    db_user = task_model.User(email=user.email, username=user.username, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user