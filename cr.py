from models import Pokemons
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select 


class CR:

    async def all(self, async_session:async_sessionmaker[AsyncSession]):
        async with async_session() as session :

            statement = select(Pokemons).order_by(Pokemons.id)

            result = await session.execute(statement)

            return result.scalars().all()
        
    async def create(self, async_session:async_sessionmaker[AsyncSession], pokemon:Pokemons):
        async with async_session() as session:

            session.add(pokemon)
            await session.commit()

    async def get_by_name_type(self, async_session:async_sessionmaker[AsyncSession], name:str, type:str):

        async with async_session() as session:

         if name==None:
            statement=select(Pokemons).filter(Pokemons.type==type)
         elif type==None:
            statement=select(Pokemons).filter(Pokemons.name==name)
         else:
            statement=select(Pokemons).filter(Pokemons.name==name, Pokemons.type==type)
            
         result=await session.execute(statement)
         return result.scalars().all()
