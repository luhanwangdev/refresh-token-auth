from pydantic import BaseModel, Field

class UserCreateRequest(BaseModel):
    username: str = Field(..., description='使用者名稱', example='Baoben')
    password: str = Field(..., description='密碼', example='password')
    age: int = Field(..., description='年齡', example='25')

class UserLoginRequest(BaseModel):
    username: str = Field(..., description='使用者名稱', example='Baoben')
    password: str = Field(..., description='密碼', example='password')

class UserResponse(BaseModel):
    username: str = Field(..., description='使用者名稱')
    access_token: str = Field(..., description='Access Token')
    refresh_token: str = Field(..., description='Refresh Token')

class UserProfileResponse(BaseModel):
    profile: str = Field(..., description='使用者資訊')
