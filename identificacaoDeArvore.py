class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Função para verificar se é uma Árvore Binária de Busca (BST)
def eh_bst(raiz, valor_min=float('-inf'), valor_max=float('inf')):
    if not raiz:
        return True
    if not (valor_min < raiz.valor < valor_max):
        return False
    return eh_bst(raiz.esquerda, valor_min, raiz.valor) and eh_bst(raiz.direita, raiz.valor, valor_max)

# Função para contar nós
def contar_nos(raiz):
    if not raiz:
        return 0
    return 1 + contar_nos(raiz.esquerda) + contar_nos(raiz.direita)

# Função para verificar se é completa
def eh_completa(raiz, indice=0, total_nos=None):
    if not raiz:
        return True
    if total_nos is None:
        total_nos = contar_nos(raiz)
    if indice >= total_nos:
        return False
    return eh_completa(raiz.esquerda, 2 * indice + 1, total_nos) and eh_completa(raiz.direita, 2 * indice + 2, total_nos)

# Função para verificar se é cheia
def eh_cheia(raiz):
    if not raiz:
        return True
    if (raiz.esquerda is None and raiz.direita is not None) or (raiz.esquerda is not None and raiz.direita is None):
        return False
    return eh_cheia(raiz.esquerda) and eh_cheia(raiz.direita)

# Função para calcular altura
def calcular_altura(raiz):
    if not raiz:
        return 0
    return 1 + max(calcular_altura(raiz.esquerda), calcular_altura(raiz.direita))

# Função para verificar se é perfeita
def eh_perfeita(raiz, profundidade=None, nivel=0):
    if not raiz:
        return True
    if not raiz.esquerda and not raiz.direita:  
        if profundidade is None:
            profundidade = nivel
        return nivel == profundidade
    if not raiz.esquerda or not raiz.direita:
        return False  
    return eh_perfeita(raiz.esquerda, profundidade, nivel + 1) and eh_perfeita(raiz.direita, profundidade, nivel + 1)

# Função principal para determinar o tipo da árvore
def tipo_arvore(raiz):
    if eh_perfeita(raiz):
        return "Árvore Perfeita"
    elif eh_cheia(raiz):
        return "Árvore Cheia"
    elif eh_completa(raiz):
        return "Árvore Completa"
    elif eh_bst(raiz):
        return "Árvore Binária de Busca"
    else:
        return "Árvore Binária"

raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)
raiz.direita.esquerda = No(6)
raiz.direita.direita = No(7)
print(tipo_arvore(raiz))
