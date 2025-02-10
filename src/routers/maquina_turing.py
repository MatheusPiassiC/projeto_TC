from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.maquina_turing_service import MaquinaTuringService

router = APIRouter()
service = MaquinaTuringService()

class MaquinaTuringCreate(BaseModel):
    estados: list
    alfabeto: list
    transicoes: dict
    estado_inicial: str
    estados_aceitacao: list

class MaquinaTuringTest(BaseModel):
    entrada: str

@router.post("/maquina_turing/criar")
async def criar_maquina_turing(maquina: MaquinaTuringCreate):
    try:
        resultado = service.criar_maquina_turing(maquina.estados, maquina.alfabeto, maquina.transicoes, maquina.estado_inicial, maquina.estados_aceitacao)
        return {"mensagem": "Máquina de Turing criada com sucesso!", "resultado": resultado}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/maquina_turing/informacoes/{nome_maquina}")
async def obter_informacoes_maquina_turing(nome_maquina: str):
    try:
        informacoes = service.obter_informacoes(nome_maquina)
        return informacoes
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/maquina_turing/testar")
async def testar_maquina_turing(maquina: MaquinaTuringTest):
    try:
        resultado = service.testar_maquina_turing(maquina.entrada)
        return {"resultado": resultado}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/maquina_turing/visualizar/{nome_maquina}")
async def visualizar_maquina_turing(nome_maquina: str):
    try:
        imagem = service.visualizar_maquina_turing(nome_maquina)
        return {"imagem": imagem}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))