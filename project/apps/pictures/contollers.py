from typing import Annotated

from fastapi import APIRouter, Query

from .services import get_photos_url


router = APIRouter(prefix='')


@router.get("/")
async def get_photos_endpoint(username: str, count: Annotated[int, Query(ge=1)]) -> dict:
    return {
        'urls': await get_photos_url(username, count)
    }
