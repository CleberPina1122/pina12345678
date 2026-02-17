from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API de Ferrovias")

# Classe para validar os dados de login
class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginData):
    if data.username == "admin" and data.password == "senha":
        return {"message": "Login bem-sucedido!"}
    else:
        return {"message": "Credenciais inválidas!"}
