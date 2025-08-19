from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

cars = [
    {
        "brand": "Nissan",
        "model": "GTR",
        "engine_volume": "3.8L",
        "power": "565 HP",
        "fuel_consumption": "11.8 L/100km",
        "transmission": "Automatic",
        "drive_type": "AWD",
    },
    {
        "brand": "BMW",
        "model": "M5",
        "engine_volume": "4.4L",
        "power": "600 HP",
        "fuel_consumption": "10.5 L/100km",
        "transmission": "Automatic",
        "drive_type": "AWD",
    }
]

brands = [
    {"brand_name": "Nissan", "brand_model": "GTR", "brand_year": 2017, "brand_color": "Black"},
    {"brand_name": "BMW", "brand_model": "M5", "brand_year": 2025, "brand_color": "White"}
]

class Car(BaseModel):
    brand: str
    model: str
    engine_volume: str
    power: str
    fuel_consumption: str
    transmission: str
    drive_type: str

class Brand(BaseModel):
    brand_name: str
    brand_model: str
    brand_year: int
    brand_color: str

@app.get("/ui", response_class=HTMLResponse)
async def main_ui(request: Request):
    return templates.TemplateResponse("ui.html", {"request": request, "cars": cars, "brands": brands})
