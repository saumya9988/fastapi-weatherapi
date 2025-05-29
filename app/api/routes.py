from fastapi import APIRouter, HTTPException
from app.schemas.weather import City
from app.services.weather_service import get_weather_data

router = APIRouter()

@router.post("/weather")
async def get_weather(city: City):
    data = get_weather_data(city.name)
    if not data:
        raise HTTPException(status_code=404, detail="City not found or API call failed")
    return data
