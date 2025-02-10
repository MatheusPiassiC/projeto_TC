from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.automato_pilha_service import AutomatoPilhaService

router = APIRouter()
servico = AutomatoPilhaService()

class CriarAutomatoPilha(BaseModel):
    estados: list
    alfabeto: list
    transicoes: dict
    estado_inicial: str
    estados_aceitacao: list

class TestarAceitacao(BaseModel):
    string: str

@router.post("/automato_pilha/criar")
async def criar_automato(automato: CriarAutomatoPilha):
    try:
        resultado = servico.criar_automato(automato.estados, automato.alfabeto, automato.transicoes, automato.estado_inicial, automato.estados_aceitacao)
        return {"mensagem": "Autômato com pilha criado com sucesso", "resultado": resultado}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/automato_pilha/{estado}")
async def recuperar_informacoes(estado: str):
    try:
        informacoes = servico.recuperar_informacoes(estado)
        return informacoes
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/automato_pilha/testar")
async def testar_aceitacao(entrada: TestarAceitacao):
    try:
        resultado = servico.testar_aceitacao(entrada.string)
        return {"aceito": resultado}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/automato_pilha/visualizar/{estado}")
async def visualizar_automato(estado: str):
    try:
        imagem = servico.visualizar_automato(estado)
        return {"imagem": imagem}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))