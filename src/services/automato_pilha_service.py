from automata.pda import pda  # Importando a classe PDA da biblioteca Automata

class AutomatoPilhaService:
    def __init__(self):
        self.automatospilha = {}

    def criar_automato(self, nome, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        automato = pda(
            states=estados,
            input_symbols=alfabeto,
            transitions=transicoes,
            initial_state=estado_inicial,
            final_states=estados_aceitacao
        )
        self.automatospilha[nome] = automato
        return automato

    def recuperar_informacoes(self, nome):
        automato = self.automatospilha.get(nome)
        if automato:
            return {
                "estados": automato.states,
                "alfabeto": automato.input_symbols,
                "transicoes": automato.transitions,
                "estado_inicial": automato.initial_state,
                "estados_aceitacao": automato.final_states
            }
        return None

    def testar_aceitacao(self, nome, string):
        automato = self.automatospilha.get(nome)
        if automato:
            return automato.accepts_input(string)
        return None

    def visualizar_automato(self, nome):
        automato = self.automatospilha.get(nome)
        if automato:
            # Aqui você pode implementar a lógica para gerar uma visualização do autômato
            # Por exemplo, usando a biblioteca de visualização que você escolher
            pass
        return None