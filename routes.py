from fastapi import APIRouter
import pandas as pd

from model_loader import model, locations
from schemas import HouseData

router = APIRouter()


# ==========================
# إرجاع جميع المناطق
# ==========================

@router.get("/locations")
def get_locations():

    return {
        "locations": locations
    }


# ==========================
# التنبؤ بالسعر
# ==========================

@router.post("/predict")
def predict_price(data: HouseData):

    input_data = {
        "location_grouped": data.location_grouped,
    "carpet_area_sqft": data.carpet_area_sqft,
    "super_area_sqft": data.super_area_sqft,
    "plot_area_sqft": data.plot_area_sqft,
    "Bathroom": data.Bathroom,
    "Balcony": data.Balcony,
    "Car Parking": data.car_parking,
    "floor_num": data.floor_num,
    "Furnishing": data.Furnishing,
    "Transaction": data.Transaction,
    "Ownership": data.Ownership,
    "Status": data.Status,
    "facing": data.facing,
    "overlooking": data.overlooking,

    # تتحسب تلقائيًا
    "has_balcony": 1 if data.Balcony > 0 else 0,
    "has_parking": 1 if data.car_parking > 0 else 0
    }

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)

    return {
        "predicted_price": float(prediction[0])
    }