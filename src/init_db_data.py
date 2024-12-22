import asyncio
from database.database import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Cheatsheet


async def populate_initial_data(session: AsyncSession):
    cheatsheets = [
        Cheatsheet(
            name="Вся школьная программа",
            callback_data="cheatsheet_1",
            file_path="src/files/allsch.pdf",
            caption="Вся школьная программа в 1 файле:",
        ),
        Cheatsheet(
            name="Дискретная математика",
            callback_data="cheatsheet_2",
            file_path="src/files/discret.pdf",
            caption="Дискретная математика в 1 файле:",
        ),
        Cheatsheet(
            name="Линейная алгебра",
            callback_data="cheatsheet_3",
            file_path="src/files/linal.pdf",
            caption="Линейная алгебра в 1 файле:",
        ),
        Cheatsheet(
            name="Математический анализ",
            callback_data="cheatsheet_4",
            file_path="src/files/mathan.pdf",
            caption="Математический анализ в 1 файле:",
        ),
    ]

    session.add_all(cheatsheets)
    await session.commit()


async def init_data():
    async with async_session() as session:
        await populate_initial_data(session=session)


if __name__ == "__main__":
    try:
        asyncio.run(init_data())
    except (KeyboardInterrupt, SystemExit):
        print('failed init')
