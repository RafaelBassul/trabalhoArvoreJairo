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



# Função para verificar se a árvore é perfeita
def eh_cheia(raiz, profundidade=None, nivel=0):
    if not raiz:
        return True
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
    fila = [(raiz, 0)]
    indice = 0
    while fila:
        no, pos = fila.pop(0)
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

    # Verifica os tipos de árvore
    if not eh_binaria(raiz):
        tipos.append("Árvore Não Binária")
    else:
        if eh_cheia(raiz):
            tipos.append("Árvore Binária Cheia")
        if eh_completa(raiz):
            tipos.append("Árvore Binária Completa")
        if not eh_cheia(raiz) and not eh_cheia(raiz) and not eh_completa(raiz):
            tipos.append("Árvore Binária")

    # Imprime os tipos encontrados
    if tipos:
        print("A árvore é:")
        for tipo in tipos:
            print(f"- {tipo}")
    else:
        print("A árvore não se encaixa em nenhum tipo específico.")

def listar_Caminhos(raiz, String):
    String += f"{raiz.valor}" + " "
    if raiz.filhos == []:
        print(String)
    for filho in raiz.filhos:
        listar_Caminhos(filho, String)

def pre_ordem(raiz):
    if raiz and eh_binaria(raiz):  
        print(raiz.valor, end=" ")  
        for filho in raiz.filhos:
            pre_ordem(filho)
    else:
        print("Não é uma árvore binária")

def pos_ordem(raiz):
    if raiz and eh_binaria(raiz): 
        for filho in raiz.filhos:
            pos_ordem(filho)
        print(raiz.valor, end=" ")  
    else:
        print("Não é uma árvore binária")

def em_ordem(raiz):
    if raiz and eh_binaria(raiz):  
        if len(raiz.filhos) > 0:
            em_ordem(raiz.filhos[0])
        print(raiz.valor, end=" ") 
        if len(raiz.filhos) > 1:
            em_ordem(raiz.filhos[1])
    else:
        print("Não é uma árvore binária")

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

print("Listagem de Caminhos:")
listar_Caminhos(raiz, "")

tipo_arvore(raiz)

print("\nPré-Ordem:")
pre_ordem(raiz)
print("\nPós-Ordem:")
pos_ordem(raiz)
print("\nEm-Ordem:")
em_ordem(raiz)
