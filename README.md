# Using (FastAPI)
A simple REST API built using FastAPI to manage users with full CRUD operations.
---
##  Features

- Create a new user
- Get all users
- Get user by ID
- Update user details
- Delete user
- Input validation using Pydantic
- SQLite database integration
- Logging support
- Unit testing
  ---
  ##  Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

-----
##Using end points
I have to  used for end points like,
      GET,
      POST,
      PUT & DELETE.
----      
##  Setup Instructions
```
git clone https://github.com//user_api.git
cd user_api

step 2: python -m venv env
step 3:  env\Scripts\activate   # Windows
step 4: Install an packages like requriments ,
         pip install -r requirements.txt
step 5:Then you have to create an .env file,
         APP_NAME=User API
         DEBUG=True
step 6: now run the server,
          uvicorn app.main:app --reload
 the Link will be contains, http://127.0.0.1:8000/docs



