from pydantic import BaseModel, Field


class HouseData(BaseModel):

    location_grouped: str

    carpet_area_sqft: float
    super_area_sqft: float
    plot_area_sqft: float

    Bathroom: int
    Balcony: int

    car_parking: int = Field(alias="Car Parking")

    floor_num: int

    Furnishing: str
    Transaction: str
    Ownership: str
    Status: str
    facing: str
    overlooking: str

    
    class Config:
        populate_by_name = True