from typing import List, Union

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: Union[str, None] = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    #owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    #items: List[Item] = []

    class Config:
        orm_mode = True