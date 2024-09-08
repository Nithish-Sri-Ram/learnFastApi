from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, Band

app=FastAPI()

BANDS = [
    {'id':1,'name':'Nithish','genre':'Melody','albums': [
        {'title':'Master of Reality','release_date':'2021-01-01'},
        {'title':'Master of Reality','release_date':'2021-01-01'},
    ]},
    {'id':2,'name':'Sam','genre':'Electronic'},
    {'id':3,'name':'Katta','genre':'Jass'},
    {'id':4,'name':'AshPari','genre':'Hip-Hop'},
]

@app.get('/')
async def index()->dict[str,str]:
    return {'hello':'world'}


@app.get('/bands')
async def bands()->list[Band]:
    #This return in a json format - since we have used pydanctic BaseModel for validation
    #for each key and value we take the value and assign it to the key
    return [
        Band(**b) for b in BANDS
    ]

@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id']==band_id),None)
    if band is None: 
        raise HTTPException(status_code=404,detail='Band not found')
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]