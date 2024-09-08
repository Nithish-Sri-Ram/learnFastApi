from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithId

app=FastAPI()

BANDS = [
    {'id':1,'name':'Nithish','genre':'Melody','albums': [
        {'title':'Master of Reality','release_date':'2021-01-01'},
        {'title':'Master of Reality','release_date':'2021-01-01'},
    ]},
    {'id':2,'name':'Sam','genre':'Rock'},
    {'id':3,'name':'Katta','genre':'Jass','albums': [
        {'title':'Master of Reality','release_date':'2021-01-01'},
        {'title':'Master of Reality','release_date':'2021-01-01'},
    ]},
    {'id':4,'name':'AshPari','genre':'Hip-Hop'},
]

@app.get('/')
async def index()->dict[str,str]:
    return {'hello':'world'}


@app.get('/bands')
async def bands(genre: GenreURLChoices | None = None, has_albums: bool = False)->list[BandWithId]:
    # we convert every model to a pydantic model 
    band_list= [BandWithId(**b) for b in BANDS]

    if genre:
        return [
            b for b in band_list if b.genre.value.lower() == genre.value
        ]
    
    if has_albums:
        return [
            b for b in band_list if len(b.albums) > 0
        ]

    return band_list

@app.get('/bands/{band_id}')
async def band(band_id: int) -> BandWithId:
    band = next((BandWithId(**b) for b in BANDS if b['id']==band_id),None)
    if band is None: 
        raise HTTPException(status_code=404,detail='Band not found')
    return band


@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithId:
    id = BANDS[-1]['id'] + 1    #The last id in the list
    band = BandWithId(id=id, **band_data.model_dump()).model_dump()  #The modelDump() method is used to convert the model to a dictionary - by taking all the user entered values
    BANDS.append(band)  # we have appended the user enterd band to our existing list 
    return band