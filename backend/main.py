from fastapi import FastAPI

app = FastAPI(title="Ferrovias API")

@app.get("/")
def root():
    return {"status": "API rodando 🚀"}

@app.get("/meu")
def meu():
    return {"eu ia": "usuário", "e-mail": "usuário.email", "é_admin": "usuário_é_admin"}

@app.get("/admin")
def admin():
    return {"status": "acesso admin liberado"}