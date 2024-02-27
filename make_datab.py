from datab import engine, myBase
import asyncio

async def make_datab():
    async with engine.begin() as c:
        from models import Pokemons

        await c.run_sync(myBase.metadata.drop_all)
        await c.run_sync(myBase.metadata.create_all)

    await engine.dispose()

asyncio.run(make_datab())