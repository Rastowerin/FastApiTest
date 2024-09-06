from fastapi import APIRouter
from redis import Redis
from starlette import status

from exceptions import AddressNotFoundException
from models import Item

router = APIRouter()

# в host указываем имя сервиса redis
redis = Redis(host='redis', port=6379, db=0)


@router.post("/write_data", status_code=status.HTTP_201_CREATED)
async def write_data(item: Item):
    redis.set(item.phone, item.address)
    return {"message": "ok"}


@router.get("/check_data", status_code=status.HTTP_200_OK)
async def check_data(phone: str):
    address = redis.get(phone)
    # возвращаем 404 если по ключу нет данных
    if not address:
        raise AddressNotFoundException
    return {"address": address}
