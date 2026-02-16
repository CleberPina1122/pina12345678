from fastapi import FastAPI, Depends
from .auth import get_current_user, require_admin
from .db import create_db_and_tables

app = FastAPI(title="API Railway")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"status": "API rodando 🚀"}

@app.get("/me")
def me(user=Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "is_admin": user.is_admin,
    }

@app.get("/admin")
def admin(user=Depends(require_admin)):
    return {"status": "acesso admin liberado"}

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("aplicativo.main:aplicativo", host="0.0.0.0", port=port)
