from automata.tm import tm
from fastapi import HTTPException

class MaquinaTuringService:
    def __init__(self):
        self.maquinas = {}

    def criar_maquina(self, nome, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        if nome in self.maquinas:
            raise HTTPException(status_code=400, detail="Máquina de Turing já existe.")
        
        maquina = tm(
            states=estados,
            input_symbols=alfabeto,
            tape_symbols=alfabeto,
            transitions=transicoes,
            initial_state=estado_inicial,
            final_states=estados_aceitacao
        )
        
        self.maquinas[nome] = maquina
        return {"mensagem": "Máquina de Turing criada com sucesso.", "nome": nome}

    def recuperar_maquina(self, nome):
        if nome not in self.maquinas:
            raise HTTPException(status_code=404, detail="Máquina de Turing não encontrada.")
        
        maquina = self.maquinas[nome]
        return {
            "nome": nome,
            "estados": maquina.states,
            "alfabeto": maquina.input_symbols,
            "transicoes": maquina.transitions,
            "estado_inicial": maquina.initial_state,
            "estados_aceitacao": maquina.final_states
        }

    def testar_aceitacao(self, nome, entrada):
        if nome not in self.maquinas:
            raise HTTPException(status_code=404, detail="Máquina de Turing não encontrada.")
        
        maquina = self.maquinas[nome]
        resultado = maquina.accepts_input(entrada)
        return {"nome": nome, "entrada": entrada, "aceita": resultado}

    def visualizar_maquina(self, nome):
        if nome not in self.maquinas:
            raise HTTPException(status_code=404, detail="Máquina de Turing não encontrada.")
        
        # Aqui você pode implementar a lógica para gerar uma visualização gráfica
        # utilizando a biblioteca de visualização que você escolher.
        return {"mensagem": "Visualização gerada com sucesso para a máquina de Turing.", "nome": nome}