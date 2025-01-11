from fastapi import Request, Response
from app.schemas import UserCreateRequest, UserLoginRequest, UserProfileResponse, UserResponse

async def login_handler(request: UserLoginRequest) -> UserResponse:
    pass

async def signup_handler(request: UserCreateRequest) -> UserResponse:
    pass

async def logout_handler(request: Request) -> Response:
    pass

async def profile_handler(request: Request) -> UserProfileResponse:
    pass
