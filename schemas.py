from enum import Enum
from pydantic import BaseModel
from datetime import date

class GenreURLChoices(Enum):
    ROCK ='rock'
    MELODY = 'melody'
    JASS = 'jass'
    HIP_HOP = 'Hip-Hop'

# the next below step is to limit the outputs

class Album(BaseModel):
    title: str
    release_date: date


# the below class is used to define the schema of the data that we are going to return aand it is inherited from BaseModel of pydantic
class Band(BaseModel):
    # {'id':1,'name':'Nithish','genre':'Melody'},
    id: int
    name: str
    genre: str
    albums: list[Album] = []

