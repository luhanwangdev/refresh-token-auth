from fastapi import FastAPI, Request, Response
from app.schemas import UserResponse, UserLoginRequest, UserCreateRequest, UserProfileResponse
from app.handlers import login_handler, logout_handler, signup_handler, profile_handler

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/signup")
async def signup(request: UserCreateRequest) -> UserResponse:
    return await signup_handler

@app.post("/login")
async def login(request: UserLoginRequest) -> UserResponse:
    return await login_handler

@app.get("/profile")
async def profile(request: Request) -> UserProfileResponse:
    return await profile_handler

@app.post("/logout")
async def logout(request: Request) -> Response:
    return await logout_handler

