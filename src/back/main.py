from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AztecMatch API is peak"}

class User(BaseModel):
    email: str
    password: str

@app.post("/register")
def register(user: User):
    return {"message": f"User {user.email} is registered!"}

@app.post("/login")
def login(user: User):
    return {"message": f"User {user.email} is logged in!"}



# =============
# PROFILE MODEL
# =============
class Profile(BaseModel):
    name: str
    age: int
    gender: str
    bio: str
    interests: str

@app.post("/profile")
def create_profile(profile: Profile):
    return {
        "message": f"Profile for {profile.name} created!",
        "profile": profile
    }

@app.get("/profile")
def get_profile():
    return {
        "profiles": [
            {
                "name": "Edwin",
                "age": 20,
                "gender": "Male",
                "bio": "Computer science student at San Diego State University.",
                "interests": "jim"
            },

            {
                "name": "Erik",
                "age": 20,
                "gender": "Female",
                "bio": "Computer science student at San Diego State University.",
                "interests": "jim"
            }
        ]
    }

