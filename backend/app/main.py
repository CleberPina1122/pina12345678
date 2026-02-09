from fastapi import FastAPI, Depends, HTTPException, Form, UploadFile, File, Body
from sqlmodel import Session, select, delete
from typing import Optional
from datetime import datetime, timezone, timedelta
import httpx

from .db import get_session, init_db
from .models import *
from .auth import require_approved_device, require_admin
from .m3u import parse_m3u, detect_stream_type
from .resolver import resolve_url
from .xmltv import parse_xmltv

app = FastAPI(title="Carbi Play API")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/channels")
def list_channels(
    q: Optional[str]=None,
    category_id: Optional[int]=None,
    group: Optional[str]=None,
    page: int=1,
    page_size: int=30,
    profile_id: Optional[int]=None,
    _dev=Depends(require_approved_device),
    session: Session = Depends(get_session)
):
    stmt = select(Channel).where(Channel.is_active == True)
    if category_id:
        stmt = stmt.where(Channel.category_id == category_id)
    if group:
        stmt = stmt.where(Channel.group == group)
    if q:
        stmt = stmt.where(Channel.name.ilike(f"%{q}%"))
    total = len(session.exec(stmt).all())
    items = session.exec(stmt.offset((page-1)*page_size).limit(page_size)).all()
    return {"items": items, "total": total}

@app.get("/categories")
def list_categories(_dev=Depends(require_approved_device), session: Session = Depends(get_session)):
    return session.exec(select(Category).order_by(Category.sort_order, Category.name)).all()
