from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db import get_session
from app.models import StockMovement, ProductInstance
from app.utils.sse import publish_event

router = APIRouter(prefix="/movements")

@router.post("/")
def create_movement(mov: StockMovement, session: Session = Depends(get_session)):
    # salvar movimento
    session.add(mov)
    # aplicar mudança no product_instance (se existir)
    if mov.instance_id:
        inst = session.get(ProductInstance, mov.instance_id)
        if inst:
            if mov.type == "entrada":
                inst.quantity = (inst.quantity or 0) + mov.qty
                inst.current_site_id = mov.to_site_id or inst.current_site_id
                inst.arrival_date = mov.timestamp
            elif mov.type == "saida":
                inst.quantity = (inst.quantity or 0) - mov.qty
                if inst.quantity <= 0:
                    inst.status = "consumed"
                    inst.current_site_id = mov.to_site_id
            session.add(inst)
    session.commit()
    # publicar evento para SSE (para dashboard)
    publish_event({"event":"movement.created","movement_id": mov.id, "product_id": mov.product_id})
    return {"ok": True, "movement_id": mov.id}
