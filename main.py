import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.postgres import database
from app.router import routes

@asynccontextmanager
async def lifespan(app:FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port="8000")