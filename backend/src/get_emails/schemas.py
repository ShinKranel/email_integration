from pydantic import BaseModel


class UserCreate(BaseModel):
    login: str
    password: str


class UserRead(BaseModel):
    login: str
