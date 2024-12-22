import asyncio
from database.database import init_db

if __name__ == "__main__":
    try:
        asyncio.run(init_db())
    except (KeyboardInterrupt, SystemExit):
        print('failed init')
