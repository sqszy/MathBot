from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import Cheatsheet


async def get_all_cheatsheets(session: AsyncSession):
    result = await session.execute(select(Cheatsheet))
    return result.scalars().all()
