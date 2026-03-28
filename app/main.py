from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

from app import crud, schemas
from app.logger import logger

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME"))

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate):
    user_id = len(crud.get_all_users()) + 1
    try:
        new_user = crud.create_user(user_id, user.name, user.email)
        logger.info(f"User created: {new_user.id}")
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users():
    logger.info("Fetching all users")
    return crud.get_all_users()


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int):
    user = crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate):
    updated_user = crud.update_user(user_id, user.name, user.email)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    logger.info(f"User updated: {user_id}")
    return updated_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted = crud.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    logger.info(f"User deleted: {user_id}")
    return {"message": "User deleted successfully"}
