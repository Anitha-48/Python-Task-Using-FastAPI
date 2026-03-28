from app.database import users_db
from app.models import User

def create_user(user_id: int, name: str, email: str):
    if user_id in users_db:
        raise ValueError("User already exists")
    user = User(user_id, name, email)
    users_db[user_id] = user
    return user

def get_all_users():
    return list(users_db.values())

def get_user(user_id: int):
    return users_db.get(user_id)

def update_user(user_id: int, name=None, email=None):
    user = users_db.get(user_id)
    if not user:
        return None
    if name:
        user.name = name
    if email:
        user.email = email
    return user

def delete_user(user_id: int):
    return users_db.pop(user_id, None)
