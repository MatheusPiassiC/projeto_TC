class Automato:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    def aceitar(self, entrada):
        estado_atual = self.estado_inicial
        for simbolo in entrada:
            if simbolo not in self.alfabeto:
                raise ValueError(f"Símbolo '{simbolo}' não está no alfabeto do autômato.")
            estado_atual = self.transicoes.get((estado_atual, simbolo))
            if estado_atual is None:
                return False
        return estado_atual in self.estados_aceitacao

    def obter_informacoes(self):
        return {
            "estados": self.estados,
            "alfabeto": self.alfabeto,
            "transicoes": self.transicoes,
            "estado_inicial": self.estado_inicial,
            "estados_aceitacao": self.estados_aceitacao,
        }