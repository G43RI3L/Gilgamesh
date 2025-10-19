from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Construction Stock SaaS")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/movements/", response_model=list[schemas.StockMovementResponse])
def list_movements(db: Session = Depends(get_db)):
    return crud.get_movements(db)

@app.post("/movements/", response_model=schemas.StockMovementResponse)
def create_movement(movement: schemas.StockMovementCreate, db: Session = Depends(get_db)):
    return crud.create_movement(db, movement)

@app.get("/stock/{site_id}")
def get_stock(site_id: int, db: Session = Depends(get_db)):
    return crud.get_stock_by_site(db, site_id)
