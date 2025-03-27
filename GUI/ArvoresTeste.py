from Arvore import No

# Árvore binária, de busca, avl, cheia
def teste1():
    root = No(50)
    child1 = No(75)
    child2 = No(25)
    child3 = No(12)
    child4 = No(37)
    child5 = No(70)
    child6 = No(80)
    root.adicionar_filho(child2)
    root.adicionar_filho(child1)
    child2.adicionar_filho(child3)
    child2.adicionar_filho(child4)
    child1.adicionar_filho(child5)
    child1.adicionar_filho(child6)

    return root

# Árvore binária, de busca, avl, completa
def teste2():
    root = No(50)
    child1 = No(75)
    child2 = No(25)
    child3 = No(12)
    child4 = No(37)
    child5 = No(70)
    root.adicionar_filho(child2)
    root.adicionar_filho(child1)
    child2.adicionar_filho(child3)
    child2.adicionar_filho(child4)
    child1.adicionar_filho(child5)
    child1.adicionar_filho(None)

    return root

# Árvore binária, de busca
def teste3():
    root = No(50)
    child1 = No(75)
    child2 = No(25)
    child3 = No(12)
    child4 = No(37)
    child5 = No(70)
    child6 = No(80)
    child7 = No(100)
    child8 = No(110)

    root.adicionar_filho(child2)
    root.adicionar_filho(child1)
    child2.adicionar_filho(child3)
    child2.adicionar_filho(child4)
    child1.adicionar_filho(child5)
    child1.adicionar_filho(child6)
    child6.adicionar_filho(None)
    child6.adicionar_filho(child7)
    child7.adicionar_filho(None)
    child7.adicionar_filho(child8)

    return root

# Árvore binária, cheia
def teste4():
    root = No(50)
    child1 = No(75)
    child2 = No(25)
    child3 = No(12)
    child4 = No(37)
    child5 = No(70)
    child6 = No(71)
    root.adicionar_filho(child2)
    root.adicionar_filho(child1)
    child2.adicionar_filho(child3)
    child2.adicionar_filho(child4)
    child1.adicionar_filho(child5)
    child1.adicionar_filho(child6)

    return root

# Árvore binária, completa
def teste5():
    root = No(50)
    child1 = No(75)
    child2 = No(25)
    child3 = No(12)
    child4 = No(37)
    child5 = No(76)
    root.adicionar_filho(child2)
    root.adicionar_filho(child1)
    child2.adicionar_filho(child3)
    child2.adicionar_filho(child4)
    child1.adicionar_filho(child5)
    child1.adicionar_filho(None)

    return root

def teste6():
    root = No(50)
    child1 = No(75)
    child2 = No(25)
    child3 = No(12)
    child4 = No(37)
    child5 = No(70)
    child6 = No(80)
    child7 = No(100)
    root.adicionar_filho(child2)
    root.adicionar_filho(child1)
    root.adicionar_filho(child7)
    child2.adicionar_filho(child3)
    child2.adicionar_filho(child4)
    child1.adicionar_filho(child5)
    child1.adicionar_filho(child6)

    return root

# Árvore só com raiz
def teste7():
    root = No(50)
    return root


# Árvore vazia
def teste8():
    root = None
    return root