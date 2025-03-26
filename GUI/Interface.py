import tkinter as tk
from tkinter import Canvas
import time
from Arvore import No
from Arvore import eh_binaria, contar_nos, calcular_altura, eh_cheia, eh_completa, \
                   tipo_arvore, listar_Caminhos, pre_ordem, pos_ordem, em_ordem, coletar_caminhos


class InterfaceArvore(tk.Tk):
    def __init__(self, tree):
        super().__init__()
        self.title("Programa de árvores")

        # Frame para os botões no top
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=10)  # Equivalente ao "padding" do css

        # Criação dos botões + atribuição de funções de cada botão
        self.button_tipo = tk.Button(self.button_frame, text="Detectar tipo da árvore", command=self.exibir_tipo)
        self.button_tipo.pack(side=tk.LEFT, padx=5)

        self.button_altura = tk.Button(self.button_frame, text="Calcular altura", command=self.exibir_altura)
        self.button_altura.pack(side=tk.LEFT, padx=5)

        self.button_caminhos = tk.Button(self.button_frame, text="Listar caminhos", command=self.exibir_caminhos)
        self.button_caminhos.pack(side=tk.LEFT, padx=5)

        self.button_preordem = tk.Button(self.button_frame, text="Pre-ordem", command=self.exibir_preordem)
        self.button_preordem.pack(side=tk.LEFT, padx=5)

        self.button_emordem = tk.Button(self.button_frame, text="Em-ordem", command=self.exibir_emordem)
        self.button_emordem.pack(side=tk.LEFT, padx=5)

        self.button_posordem = tk.Button(self.button_frame, text="Pos-ordem", command=self.exibir_posordem)
        self.button_posordem.pack(side=tk.LEFT, padx=5)


        # Cria um "canvas" para visualizar árvore
        self.canvas = Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()

        # Label que é usada por algumas funções
        self.label = tk.Label(self, text=" ", font=('Arial', 12, 'italic'), bg="lightgray", width=100)
        self.label.pack(pady=5)

        self.tree = tree
        self.ovals = {}
        InterfaceArvore.path_counter = 0

        self.draw_tree(self.tree, 400, 50, 150, 50)

    def exibir_preordem(self, raiz=None, resultado=None):
        if raiz is None and self.tree:
            raiz = self.tree
        if resultado is None:
            resultado = []
        if raiz and eh_binaria(raiz):  
            resultado.append(str(raiz.valor))
            for filho in raiz.filhos:
                self.exibir_preordem(filho, resultado)
        else:
            resultado.clear()
            resultado.append("Não é uma árvore binária")
        texto_resultado = " - ".join(resultado)
        self.label.config(text=f"Pre-ordem: {texto_resultado}")

    def exibir_posordem(self, raiz=None, resultado=None):
        if raiz is None and self.tree:
            raiz = self.tree
        if resultado is None:
            resultado = []
        if raiz and eh_binaria(raiz):  
            for filho in raiz.filhos:
                self.exibir_posordem(filho, resultado)
            resultado.append(str(raiz.valor))
        else:
            resultado.clear()
            resultado.append("Não é uma árvore binária")
        texto_resultado = " - ".join(resultado)
        self.label.config(text=f"Pos-ordem: {texto_resultado}")
    
    def exibir_emordem(self, raiz=None, resultado=None):
        if raiz is None and self.tree:
            raiz = self.tree
        if resultado is None:
            resultado = []
        if raiz and eh_binaria(raiz): 
            if len(raiz.filhos) > 0:
                self.exibir_emordem(raiz.filhos[0], resultado)
            resultado.append(str(raiz.valor))
            if len(raiz.filhos) > 1:
                self.exibir_emordem(raiz.filhos[1], resultado)
        else:
            resultado.clear()
            resultado.append("Não é uma árvore binária")
        texto_resultado = " - ".join(resultado)
        self.label.config(text=f"Em-ordem: {texto_resultado}")

    def exibir_caminhos(self):
        paths = []
        coletar_caminhos(self.tree, paths)

        Strings = []
        for s in listar_Caminhos(self.tree, ""):
            Strings.append(s)

        self.reset_graph()
        if InterfaceArvore.path_counter == len(paths):
            InterfaceArvore.path_counter = 0
            self.label.config(text="")
        else:
            n = InterfaceArvore.path_counter
            for no in paths[n]:
                ball_id = self.ovals[f"{no.id}"]
                self.canvas.itemconfig(ball_id, fill='red')
            texto_caminho = f"Caminho destacado: {Strings[n]}"
            self.label.config(text=texto_caminho)
            InterfaceArvore.path_counter += 1
            
    def exibir_altura(self):
        altura = calcular_altura(self.tree)
        n_nos = contar_nos(self.tree)

        texto = f"A árvore possui {n_nos} nós,\ne tem altura {altura}."
        self.label.config(text=texto)

    def exibir_tipo(self):
        tipos = tipo_arvore(self.tree)
        string_tipos = "Os tipos da árvore:\n"

        # Imprime os tipos encontrados
        if tipos:
            for tipo in tipos:
                string_tipos += f"- {tipo}\n"
        else:
            string_tipos = "Árvore inválida, nenhum tipo detectado."

        self.label.config(text=string_tipos)

    def draw_tree(self, node, x, y, x_offset, y_offset):
        # Desenha linhas para nós filhos
        for i, child in enumerate(node.filhos):
            child_x = x + (i - len(node.filhos) // 2) * x_offset
            child_y = y + y_offset
            self.canvas.create_line(x, y, child_x, child_y, arrow=tk.LAST)

            # Recursivamente desenha a árvore filha
            self.draw_tree(child, child_x, child_y, x_offset // 2, y_offset)

        # Desenha as bolinhas com o texto
        oval_id = self.canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightblue', outline='black')
        self.canvas.create_text(x, y, text=node.valor, font=('Arial', 10, 'bold'))

        # Armazena a referência para a bolinha desenhada
        self.ovals[f"{node.id}"] = oval_id

    def reset_graph(self):
        self.canvas.delete("all")
        self.draw_tree(self.tree, 400, 50, 150, 50)

# Árvore de teste (alterar árvore aqui)
root = No(50)
child1 = No(75)
child2 = No(25)
child3 = No(12)
child4 = No(37)
child5 = No(100)
child6 = No(34)
child7 = No(70)
child8 = No(80)
child9 = No(87)
root.adicionar_filho(child2)
root.adicionar_filho(child1)
#root.adicionar_filho(child5)
#root.adicionar_filho(child6)
child2.adicionar_filho(child3)
child2.adicionar_filho(child4)
child1.adicionar_filho(child7)
child1.adicionar_filho(child8)
#child3.adicionar_filho(child9)


# Carregar / Abrir interface gráfica
app = InterfaceArvore(root)
app.mainloop()