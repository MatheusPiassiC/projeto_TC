from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.pda import PDA
from automata.tm import TuringMachine
import matplotlib.pyplot as plt
import networkx as nx

def visualizar_afd(afd: DFA, nome_arquivo: str):
    grafo = nx.DiGraph()
    
    for estado in afd.states:
        grafo.add_node(estado)
    
    for transicao in afd.transitions:
        origem, simbolo = transicao
        destino = afd.transitions[transicao]
        grafo.add_edge(origem, destino, label=simbolo)
    
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, arrows=True)
    edge_labels = nx.get_edge_attributes(grafo, 'label')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)
    
    plt.title("Visualização do AFD")
    plt.savefig(nome_arquivo)
    plt.close()

def visualizar_nfa(nfa: NFA, nome_arquivo: str):
    grafo = nx.DiGraph()
    
    for estado in nfa.states:
        grafo.add_node(estado)
    
    for transicao in nfa.transitions:
        origem, simbolo = transicao
        destinos = nfa.transitions[transicao]
        for destino in destinos:
            grafo.add_edge(origem, destino, label=simbolo)
    
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, arrows=True)
    edge_labels = nx.get_edge_attributes(grafo, 'label')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)
    
    plt.title("Visualização do NFA")
    plt.savefig(nome_arquivo)
    plt.close()

def visualizar_pda(pda: PDA, nome_arquivo: str):
    # Implementar visualização para autômatos com pilha
    pass

def visualizar_maquina_turing(maquina: TuringMachine, nome_arquivo: str):
    # Implementar visualização para máquinas de Turing
    pass