class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []  # Lista de filhos (suporta mais de dois)

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

# Função para verificar se a árvore é binária
def eh_binaria(raiz):
    if not raiz:
        return True
    if len(raiz.filhos) > 2:
        return False
    return all(eh_binaria(filho) for filho in raiz.filhos)

# Função para contar nós
def contar_nos(raiz):
    if not raiz:
        return 0
    return 1 + sum(contar_nos(filho) for filho in raiz.filhos)

# Função para calcular altura
def calcular_altura(raiz):
    if not raiz:
        return 0
    return 1 + max((calcular_altura(filho) for filho in raiz.filhos), default=0)

# Função para verificar se a árvore é cheia
def eh_cheia(raiz):
    if not raiz:
        return True
    qtd_filhos = len(raiz.filhos)
    if qtd_filhos > 0 and any(len(filho.filhos) not in [0, qtd_filhos] for filho in raiz.filhos):
        return False
    return all(eh_cheia(filho) for filho in raiz.filhos)

# Função para verificar se a árvore é perfeita
def eh_perfeita(raiz, profundidade=None, nivel=0):
    if not raiz:
        return True
    if not raiz.filhos:  # Se for folha
        if profundidade is None:
            profundidade = nivel
        return nivel == profundidade
    if any(len(filho.filhos) != len(raiz.filhos[0].filhos) for filho in raiz.filhos):
        return False
    return all(eh_perfeita(filho, profundidade, nivel + 1) for filho in raiz.filhos)

# Função para verificar se a árvore é completa
def eh_completa(raiz):
    fila = [(raiz, 0)]
    total_nos = contar_nos(raiz)
    indice = 0
    while fila:
        no, pos = fila.pop(0)
        if pos != indice:
            return False
        for filho in no.filhos:
            fila.append((filho, 2 * pos + 1))
        indice += 1
    return True

# Função principal para determinar o tipo da árvore
def tipo_arvore(raiz):
    if not eh_binaria(raiz):
        return "Árvore Não Binária"
    if eh_perfeita(raiz):
        return "Árvore Binária Perfeita"
    elif eh_cheia(raiz):
        return "Árvore Binária Cheia"
    elif eh_completa(raiz):
        return "Árvore Binária Completa"
    else:
        return "Árvore Binária"

raiz = No(1)
filho2 = No(2)
filho3 = No(3)
filho4 = No(4)
filho5 = No(5)
filho6 = No(6)
filho7 = No(7)
filho_extra = No(8)

raiz.adicionar_filho(filho2)
raiz.adicionar_filho(filho3)
#raiz.adicionar_filho(filho4)  # Descomentar esta linha para tornar a árvore nao binária

filho2.adicionar_filho(filho5)
filho2.adicionar_filho(filho6)
filho3.adicionar_filho(filho7)
print(tipo_arvore(raiz)) 
