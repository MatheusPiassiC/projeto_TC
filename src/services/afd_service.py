from automata.fa.dfa import DFA
from typing import Dict, Any, List

class AFDService:
    def __init__(self):
        self.afds: Dict[str, DFA] = {}

    def criar_afd(self, nome: str, estados: List[str], alfabeto: List[str], transicoes: Dict[str, Dict[str, str]], estado_inicial: str, estados_aceitacao: List[str]) -> str:
        afd = DFA(
            states=set(estados),
            input_symbols=set(alfabeto),
            transitions=transicoes,
            initial_state=estado_inicial,
            final_states=set(estados_aceitacao)
        )
        self.afds[nome] = afd
        return f"AFD '{nome}' criado com sucesso."

    def recuperar_informacoes(self, nome: str) -> Dict[str, Any]:
        afd = self.afds.get(nome)
        if afd:
            return {
                "estados": list(afd.states),
                "alfabeto": list(afd.input_symbols),
                "transicoes": afd.transitions,
                "estado_inicial": afd.initial_state,
                "estados_aceitacao": list(afd.final_states)
            }
        else:
            return {"erro": "AFD não encontrado."}

    def testar_aceitacao(self, nome: str, string: str) -> bool:
        afd = self.afds.get(nome)
        if afd:
            return afd.accepts_input(string)
        else:
            return False

    def visualizar_afd(self, nome: str) -> str:
        afd = self.afds.get(nome)
        if afd:
            # Aqui você pode implementar a lógica para gerar uma visualização gráfica
            # utilizando a biblioteca de visualização que você escolher.
            return f"Visualização do AFD '{nome}' gerada com sucesso."
        else:
            return "AFD não encontrado."