import asyncpg
import asyncio
import os
from dotenv import load_dotenv

# DB_USER = 'postgres'
# DB_PASSWORD = 'my_password'
# DB_DATABASE  = 'postgres_test'
# DB_HOST = 'localhost'
# DB_PORT = '5432'

# DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
load_dotenv()
DB_URL = os.getenv('DB_URL')

class PostgresConnection:
    def __init__(self, db_url:str):
        self.db_url = db_url

    async def connect(self):
        self.pool = await asyncpg.create_pool(self.db_url)

    async def disconnect(self):
        self.pool.close()

database = PostgresConnection(DB_URL)