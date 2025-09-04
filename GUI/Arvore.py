class No:
    _Id_counter = 0

    def __init__(self, valor):
        self.id = No._Id_counter
        No._Id_counter += 1
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
    return 1 + max((calcular_altura(filho) for filho in raiz.filhos), default=-1)

# Função para verificar se a árvore é cheia
def eh_cheia(raiz, profundidade=None, nivel=0):
    if not raiz:
        return False
    # Se o nó for folha
    if not raiz.filhos:
        if profundidade is None:
            profundidade = nivel
        return nivel == profundidade
    # Se o nó tem filhos, deve ter exatamente 2 filhos
    if len(raiz.filhos) != 2:
        return False
    # Verificar recursivamente todos os filhos
    return all(eh_cheia(filho, profundidade, nivel + 1) for filho in raiz.filhos)

# Função para verificar se a árvore é completa
def eh_completa(raiz):
    if raiz is None:
        return True
    else:
        fila = [(raiz, 0)]
        indice = 0
        while fila:
            no, pos = fila.pop(0)
            if no is not None:   
                if pos != indice:
                    return False
                for i, filho in enumerate(no.filhos):
                    new_pos = 2 * pos + 1 + i
                    fila.append((filho, new_pos))
                indice += 1
        return True

# Função principal para determinar o tipo da árvore
def tipo_arvore(raiz):
    tipos = []

    ## Verifica os tipos de árvore
    if not eh_binaria(raiz):
        tipos.append("Árvore Não Binária")
    else:
        if eh_cheia(raiz):
            tipos.append("Árvore Binária Cheia")
        if eh_completa(raiz) and not eh_cheia(raiz):
            tipos.append("Árvore Binária Completa")
        if eh_bst(raiz):
            tipos.append("Árvore Binária de Busca")
            if eh_avl(raiz):
                tipos.append("Árvore Binária de Busca Balanceada")

        if not eh_cheia(raiz) and not eh_cheia(raiz) and not eh_completa(raiz) and not eh_bst(raiz):
            tipos.append("Árvore Binária")

    return tipos

def listar_Caminhos(raiz, String):
    if raiz is None:
        return
    String += f"{raiz.valor}" + " - "
    if raiz.filhos == []:
        yield String[:-2]
    else:
        for filho in raiz.filhos:
            yield from listar_Caminhos(filho, String)

def coletar_caminhos(raiz, paths, path=None):
    if raiz is None:
        return
    if path is None:
        path = []
    path.append(raiz)
    if raiz.filhos == []:
        paths.append(path.copy())
    for filho in raiz.filhos:
        coletar_caminhos(filho, paths, path.copy())

def calcular_altura_para_função(raiz):
    if not raiz:
        return 0
    return 1 + max((calcular_altura_para_função(filho) for filho in raiz.filhos), default=0)

# Função para verificar se a árvore é BST
def eh_bst(raiz, minimo=float('-inf'), maximo=float('inf')):
    if not raiz:
        return True
    if not (minimo < raiz.valor < maximo):
        return False
    if len(raiz.filhos) > 2:
        return False  # Se tem mais de dois filhos, não pode ser BST
    esquerda = raiz.filhos[0] if len(raiz.filhos) > 0 else None
    direita = raiz.filhos[1] if len(raiz.filhos) > 1 else None
    return eh_bst(esquerda, minimo, raiz.valor) and eh_bst(direita, raiz.valor, maximo)

# Função para verificar se a árvore é AVL
def eh_avl(raiz):
    if not raiz:
        return True
    if len(raiz.filhos) > 2:
        return False  # Se tem mais de dois filhos, não pode ser AVL
    esquerda = raiz.filhos[0] if len(raiz.filhos) > 0 else None
    direita = raiz.filhos[1] if len(raiz.filhos) > 1 else None
    altura_esq = calcular_altura_para_função(esquerda)
    altura_dir = calcular_altura_para_função(direita)
    if abs(altura_esq - altura_dir) > 1:
        return False
    return eh_avl(esquerda) and eh_avl(direita)
