from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import afd, automato_pilha, maquina_turing

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo os routers
app.include_router(afd.router, prefix="/afd", tags=["AFD"])
app.include_router(automato_pilha.router, prefix="/automato-pilha", tags=["Autômatos com Pilha"])
app.include_router(maquina_turing.router, prefix="/maquina-turing", tags=["Máquinas de Turing"])

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API de Autômatos!"}