from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Site(Base):
    __tablename__ = "sites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    unit = Column(String)  # ex: kg, m², unidade
    qr_code = Column(String, unique=True)

class StockMovement(Base):
    __tablename__ = "stock_movements"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    site_id = Column(Integer, ForeignKey("sites.id"))
    quantity = Column(Float)
    movement_type = Column(String)  # "entrada" ou "saida"
    date = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")
    site = relationship("Site")
