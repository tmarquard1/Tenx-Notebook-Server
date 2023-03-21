from typing import List, Union

from pydantic import BaseModel

from . import models

# https://stackoverflow.com/questions/68626930/fastapi-many-to-many-response-schema-and-relationship

class TagBase(BaseModel):
    tag: str

    class Meta:
        orm_model = models.Tag

    class Config:
        orm_mode = True

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True
    
    

class NoteBase(BaseModel):
    title: str
    content: Union[str, None] = None
    tags: List[TagBase] = []
    class Config:
        orm_mode = True

class NoteCreate(NoteBase):
    #tags = List[Tag]
    pass

class Note(NoteBase):
    id: int

    class Config:
        orm_mode = True
    

class NoteOut(Note):
    tags: List[Tag]

class NoteIn(Note):
    tags: List[TagCreate]

#class TagOut(Tag):
#    notes: List[Note]

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