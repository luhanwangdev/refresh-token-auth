from fastapi import FastAPI, Request, Response
from app.schemas import UserResponse, UserLoginRequest, UserCreateRequest, UserProfileResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/signup")
def signup(request: UserCreateRequest) -> UserResponse:
    return {"Hello": "World"}

@app.post("/login")
def login(request: UserLoginRequest) -> UserResponse:
    return {"Hello": "World"}

@app.get("/profile")
def profile(request: Request) -> UserProfileResponse:
    return {"Hello": "World"}

@app.get("/logout")
def logout(request: Request) -> Response:
    return {"Hello": "World"}

