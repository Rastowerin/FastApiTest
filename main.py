from fastapi import FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from endpoints import router
from exceptions import AddressNotFoundException

app = FastAPI()
app.include_router(router)


# добавляем exception handler, что бы вынести лишнюю логику из эндпоинтов
@app.exception_handler(AddressNotFoundException)
async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )
