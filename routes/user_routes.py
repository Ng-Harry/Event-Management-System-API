from fastapi import APIRouter, HTTPException
from typing import List
from schemas.models import User, UserCreate
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])
user_service = UserService()

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    return user_service.create_user(user)

@router.get("/", response_model=List[User])
def get_users():
    return user_service.get_all_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    updated_user = user_service.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}")
def delete_user(user_id: int):
    if not user_service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@router.patch("/{user_id}/deactivate", response_model=User)
def deactivate_user(user_id: int):
    user = user_service.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user 