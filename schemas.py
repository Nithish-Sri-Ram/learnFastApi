from enum import Enum
from pydantic import BaseModel, validator
from datetime import date

class GenreURLChoices(Enum):
    ROCK ='rock'
    MELODY = 'melody'
    JASS = 'jass'
    HIP_HOP = 'hip-hop'

#this below class I'm using to validate the input of gneres
class GenreChoices(Enum):
    ROCK ='Rock'
    MELODY = 'Melody'
    JASS = 'Jass'
    HIP_HOP = 'Hip-Hop'

# the next below step is to limit the outputs

class Album(BaseModel):
    title: str
    release_date: date


# Instead of this single model we are going to have a variety of models
# class Band(BaseModel):
#     id: int
#     name: str
#     genre: str
#     albums: list[Album] = []


class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Album] = []

class BandCreate(BandBase):
    @validator('genre',pre=True)
    def title_case_genre(cls, value):
        return value.title()        #RoCk -> Rock

class BandWithId(BandBase):
    id: int