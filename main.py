from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router


app = FastAPI(
    title="House Price Prediction API",
    version="1.0"
)


# السماح للـ Frontend بالتواصل مع الـ Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # هنخليها مفتوحة أثناء التطوير
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# إضافة جميع الـ Routes
app.include_router(router)