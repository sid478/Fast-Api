from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Address(BaseModel):
    state:str
    city:str
    

class User(BaseModel):
    name:str
    age:int
    address:Address
   

@app.get("/")
def home():
    return {"message": "School FastAPI is running!"}

@app.get("/student")
def get_student():
    return {"message": "This is a student student!"}



@app.get("/users/{user_id}")
def get_users(user_id:int):
    return {"User id": user_id}

@app.get("/school")
def get_school(name :str = None,price:int=0):
    return{"school Name": name, "price": price}


@app.post("/user-create")
def create_user(user:User):
    return{
        "message": "User created successfully",
        "User":user
    }