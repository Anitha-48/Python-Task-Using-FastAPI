# Using (FastAPI)
A simple REST API built using FastAPI to manage users with full CRUD operations.
---
##  Features

- Create a new user
- Get all users
- Get user by ID
- Update user details
- Delete user
- Logging support
- Unit testing
  ---
  ##  Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

-----
## Using end points like,
      GET,
      POST,
      PUT & DELETE.

##  Setup Instructions
```
step 1:
https://github.com/Anitha-48/Python-Task-Using-FastAPI/
cd /Python-Task-Using-FastAPI/

step 2: python -m venv env
step 3:  env\Scripts\activate   
step 4: Install an packages like requriments ,
         pip install -r requirements.txt
step 5:Then you have to create an .env file,
         APP_NAME=User API
         DEBUG=True
step 6: now run the server,
          uvicorn app.main:app --reload
 It should be open an empty page,  http://127.0.0.1:8000
 then used the link,
 http://127.0.0.1:8000/docs



