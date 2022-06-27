from fastapi import APIRouter
from typing import Union
from app.core.src.models.property import PropertyModel

router = APIRouter(
    prefix="/properties",
    tags=["Property"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_list(limit: Union[int, None] = 100, year: Union[int, None] = None, city: str = None, address: str = None):
    filter = {"limit": limit, "year": year, "city": city, "address": address}
    properties = PropertyModel.properties(filter)
    if len(properties) == 0:
        return "No avaiable items for this request"
    return properties


@router.get("/{property_id}")
async def read_single(property_id: int):
    property = PropertyModel.property(property_id)
    if len(property) == 0:
        return "No item available"
    return property
