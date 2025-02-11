from fastapi import FastAPI
from src.routers import afd, automato_pilha, maquina_turing

app = FastAPI()

# Incluindo os routers
app.include_router(afd.router, prefix="/afd", tags=["AFD"])
app.include_router(automato_pilha.router, prefix="/automato-pilha", tags=["Autômatos com Pilha"])
app.include_router(maquina_turing.router, prefix="/maquina-turing", tags=["Máquinas de Turing"])

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API de Autômatos!"}