import joblib
import json


# تحميل أفضل موديل
model = joblib.load("house_price_model.pkl")


# تحميل قائمة المناطق
with open("locations.json", "r") as file:
    locations = json.load(file)

