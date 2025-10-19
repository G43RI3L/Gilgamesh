from pydantic import BaseModel
from datetime import datetime

class StockMovementBase(BaseModel):
    product_id: int
    site_id: int
    quantity: float
    movement_type: str

class StockMovementCreate(StockMovementBase):
    pass

class StockMovementResponse(StockMovementBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True
