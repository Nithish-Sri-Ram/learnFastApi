from fastapi import FastAPI, HTTPException
from enum import Enum

app=FastAPI()

class GenreURLChoices(Enum):
    ROCK ='rock'
    MELODY = 'melody'
    JASS = 'jass'
    HIP_HOP = 'Hip-Hop'

BANDS = [
    {'id':1,'name':'Nithish','genre':'Melody'},
    {'id':2,'name':'Sam','genre':'Electronic'},
    {'id':3,'name':'Katta','genre':'Jass'},
    {'id':4,'name':'AshPari','genre':'Hip-Hop'},
]

@app.get('/')
async def index()->dict[str,str]:
    return {'hello':'world'}


@app.get('/bands')
async def bands()->list[dict]:
    return BANDS

@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    #the pythons next argument takes 2 parameters - the first one is an iterable
    band = next((b for b in BANDS if b['id']==band_id),None)    #The second is a default item if not found
    if band is None: 
        # pass
        raise HTTPException(status_code=404,detail='Band not found')
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    #we could also take any string value as input but with the above validation done 
    # we could accept only the pre defined values
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]