from fastapi import FastAPI
from redis import Redis
from sqlmodel import SQLModel
from starlette import status

app = FastAPI()

redis = Redis(host='localhost', port=6379, db=0)


class Item(SQLModel):
    phone: str
    address: str


@app.post("/write_data", status_code=status.HTTP_200_OK)
async def write_data(item: Item):
    a = redis.set(item.phone, item.address)
    return {"message": "ok"}


@app.get("/check_data", status_code=status.HTTP_200_OK)
async def check_data(phone: str):
    address = redis.get(phone)
    return {"address": address}
