from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.afd_service import AFDService

router = APIRouter()
afd_service = AFDService()

class CriarAFDRequest(BaseModel):
    nome: str
    estados: list
    alfabeto: list
    transicoes: dict
    estado_inicial: str
    estados_aceitacao: list

class TestarAceitacaoRequest(BaseModel):
    nome: str
    string: str

@router.post("/criar")
async def criar_afd(afd_request: CriarAFDRequest):
    mensagem = afd_service.criar_afd(
        afd_request.nome,
        afd_request.estados,
        afd_request.alfabeto,
        afd_request.transicoes,
        afd_request.estado_inicial,
        afd_request.estados_aceitacao
    )
    return {"message": mensagem}

@router.get("/{afd_id}")
async def recuperar_afd(afd_id: str):
    afd = afd_service.recuperar_informacoes(afd_id)
    if "erro" in afd:
        raise HTTPException(status_code=404, detail=afd["erro"])
    return afd

@router.post("/testar")
async def testar_aceitacao(request: TestarAceitacaoRequest):
    resultado = afd_service.testar_aceitacao(request.nome, request.string)
    return {"resultado": resultado}

@router.get("/{afd_id}/visualizar")
async def visualizar_afd(afd_id: str):
    mensagem = afd_service.visualizar_afd(afd_id)
    if mensagem == "AFD não encontrado.":
        raise HTTPException(status_code=404, detail=mensagem)
    return {"message": mensagem}