from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models import Product, StockMovement
import os
import httpx
import json

router = APIRouter(prefix="/chat")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@router.get("/query")
async def chat_query(q: str, tenant_id: str, session: Session = Depends(get_session)):
    """
    Ex.: q="quantas sacas de cimento tenho na obra X?"
    - Aqui fazemos: parse simples, consultamos DB, retornamos resposta já com dados.
    - Não armazenamos a pergunta nem o prompt.
    """
    # *** EXEMPLO SIMPLIFICADO: procurar palavra 'cimento' no product name ***
    stmt = select(Product).where(Product.tenant_id == tenant_id)
    prods = session.exec(stmt).all()
    matching = [p for p in prods if "cimento" in (p.name or "").lower() or "cimento" in (q.lower())]
    if not matching:
        # fallback: perguntar ao OpenAI (opcional) — mas primeiro tentamos dados locais
        return {"text":"Nenhum produto encontrado com esse nome."}
    product = matching[0]
    # calcular estoque atual simples: somar movimentos
    stmt2 = select(StockMovement).where(StockMovement.product_id == product.id, StockMovement.tenant_id == tenant_id)
    moves = session.exec(stmt2).all()
    total = sum([m.qty if m.type=="entrada" else -m.qty for m in moves])
    # montar resposta direta (não gravamos a pergunta)
    text = f"Produto: {product.name}\nEstoque atual aproximado: {total} {product.unit}"
    # opcional: chamar OpenAI para formatar o texto sem enviar dados sensíveis; aqui já retornamos o texto
    return {"text": text, "product_id": product.id, "stock": total}
