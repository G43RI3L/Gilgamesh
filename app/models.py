from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid

class Tenant(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    name: str

class Site(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    tenant_id: str
    name: str
    address: Optional[str] = None

class Product(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    tenant_id: str
    sku: str
    name: str
    unit: str
    default_min_stock: Optional[int] = 0
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ProductInstance(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    tenant_id: str
    product_id: str
    lot: Optional[str] = None
    manufacture_date: Optional[str] = None
    arrival_date: Optional[datetime] = None
    current_site_id: Optional[str] = None
    quantity: float = 1.0
    status: Optional[str] = "active"
    metadata: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class StockMovement(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    tenant_id: str
    product_id: str
    instance_id: Optional[str] = None
    type: str  # 'entrada'|'saida'|'transfer'
    qty: float
    from_site_id: Optional[str] = None
    to_site_id: Optional[str] = None
    user: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    proof_url: Optional[str] = None
    reference: Optional[str] = None
    client_timestamp: Optional[datetime] = None
