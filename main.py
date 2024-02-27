from fastapi import FastAPI, HTTPException
from cr import CR 
from sqlalchemy.ext.asyncio import async_sessionmaker
from datab import engine
import requests
from models import Pokemons
from serializers import PokoModel
from typing import List, Optional
from dotenv import load_dotenv
import os

load_dotenv()

limit=os.getenv('limit')




db=CR()

session=async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

app= FastAPI()



@app.get('/api/{version}/pokemons')
async def show_all_pokemons(version: str, name: Optional[str]=None, type: Optional[str]=None):

    if version!='v1':
        return {"Message" : "Sorry! Only version 1 is available for now. Please enter 'v1' in the version section to access it."}

    try:
        pokemons = await db.all(session)  
        
    except Exception as e:
        print(f"\nError fetching pokemons: {e}")
        raise HTTPException(status_code=500, detail="Error fetching pokemons from the database")

    if not list(pokemons):

        print("\nNo pokemons found. Fetching from API....\n")

        allPokemons=await fetch_from_api(version)


        for eachPokemon in allPokemons:

            pokoInstance=Pokemons(id=str(eachPokemon['id']), name=eachPokemon['name'], image=eachPokemon['image'], type=eachPokemon['type'])

            try:
             await db.create(session, pokemon=pokoInstance)
            except Exception as e:
                print(f"\nError creating pokemon: {e}\n")

        pokemons=await db.all(session)
    



        
    else:
        print(f"\nPokemons exist!\n")
        
    
    if name!=None or type!=None:
        pokemons=await db.get_by_name_type(session, name=name, type=type)


    return pokemons




async def fetch_from_api(version):


    poke_version=None

    if version == 'v1':
        poke_version='v2'
    else:
        return

    
    url=f"https://pokeapi.co/api/{poke_version}/pokemon?limit={limit}"
    response=requests.get(url)
    data=response.json()

    allPokemons=[]
    
    for each in data['results']:
        thisPokemon={}
        holder=''

        thisPokemon['name']=each['name']

        otherInfo=requests.get(each['url'])
        infos=otherInfo.json()

        thisPokemon['id']=infos['id']
        
        for eachType in infos["types"]:
            holder+= eachType["type"]['name']+", "
        
        thisPokemon['type']=holder[:-2]

        thisPokemon['image']=infos['sprites']['front_default']

        allPokemons.append(thisPokemon)

        
        
    print(allPokemons)
        

    return allPokemons
    
    


