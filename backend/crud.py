from sqlalchemy.orm import Session
from . import models, schemas

def create_movement(db: Session, movement: schemas.StockMovementCreate):
    db_movement = models.StockMovement(**movement.dict())
    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)
    return db_movement

def get_movements(db: Session):
    return db.query(models.StockMovement).all()

def get_stock_by_site(db: Session, site_id: int):
    return db.query(models.StockMovement).filter(models.StockMovement.site_id == site_id).all()
