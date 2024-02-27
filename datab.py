import os
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase

load_dotenv()


engine= create_async_engine(
    url=os.getenv("db_url"),
    echo=True
)

class myBase(DeclarativeBase):
    pass