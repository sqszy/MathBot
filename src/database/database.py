import os
from sqlalchemy.orm import sessionmaker
from config.config import DB_URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from .models import Base


DB = f"sqlite+aiosqlite:///{DB_URL}/math_bot.db"

engine = create_async_engine(DB, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    print(DB)
    if not os.path.exists(DB_URL):
        os.makedirs(DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
