from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db import get_session
from app.models import Product, ProductInstance
from app.utils.qr import generate_qr_base64

router = APIRouter(prefix="/products")

@router.post("/")
def create_product(product: Product, session: Session = Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.post("/{product_id}/generate-qr")
def generate_qr(product_id: str, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        return {"error":"product not found"}
    # Gerar QR para nova instância (unit)
    instance = ProductInstance(tenant_id=product.tenant_id, product_id=product.id, quantity=1.0)
    session.add(instance)
    session.commit()
    session.refresh(instance)
    payload = {
        "type": "item",
        "tenant": product.tenant_id,
        "product_id": product.id,
        "id": instance.id
    }
    import json
    b64 = generate_qr_base64(json.dumps(payload))
    return {"instance": instance, "qr": b64}
