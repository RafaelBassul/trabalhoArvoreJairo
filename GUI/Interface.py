import tkinter as tk
from tkinter import Canvas
from Arvore import eh_binaria, contar_nos, calcular_altura, tipo_arvore, listar_Caminhos, coletar_caminhos
from ArvoresTeste import teste1, teste2, teste3, teste4, teste5, teste6, teste7, teste8


class InterfaceArvore(tk.Tk):
    def __init__(self, tree=None):
        super().__init__()
        self.title("Programa de árvores")

        if tree is None:
            arvVazia = "Árvore vazia\n Tipos: Binária balanceada cheia\n"
            arvVazia += " Altura: 0\n Incapaz de percorrer caminhos ou percurso"
            self.label = tk.Label(self, text=arvVazia, font=('Arial', 12, 'italic'), bg="lightgray", width=100)
            self.label.pack(pady=5)
            return

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

        self.button_preordem = tk.Button(self.button_frame, text="Pre-ordem", command=lambda:self.exibir_preordem(self.tree))
        self.button_preordem.pack(side=tk.LEFT, padx=5)

        self.button_emordem = tk.Button(self.button_frame, text="Em-ordem", command=lambda:self.exibir_emordem(self.tree))
        self.button_emordem.pack(side=tk.LEFT, padx=5)

        self.button_posordem = tk.Button(self.button_frame, text="Pos-ordem", command=lambda:self.exibir_posordem(self.tree))
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

    def exibir_preordem(self, raiz, resultado=None):
        self.reset_graph()
        InterfaceArvore.path_counter = 0

        if raiz is None:
            return
        if resultado is None:
            resultado = []
        if eh_binaria(raiz):  
            resultado.append(str(raiz.valor))
            for filho in raiz.filhos:
                self.exibir_preordem(filho, resultado)
        else:
            resultado.clear()
            resultado.append("Não é uma árvore binária")
        texto_resultado = " - ".join(resultado)
        self.label.config(text=f"Pre-ordem: {texto_resultado}")

    def exibir_posordem(self, raiz, resultado=None):
        self.reset_graph()
        InterfaceArvore.path_counter = 0

        if raiz is None:
            return
        if resultado is None:
            resultado = []
        if eh_binaria(raiz):  
            for filho in raiz.filhos:
                self.exibir_posordem(filho, resultado)
            resultado.append(str(raiz.valor))
        else:
            resultado.clear()
            resultado.append("Não é uma árvore binária")
        texto_resultado = " - ".join(resultado)
        self.label.config(text=f"Pos-ordem: {texto_resultado}")
    
    def exibir_emordem(self, raiz, resultado=None):
        self.reset_graph()
        InterfaceArvore.path_counter = 0

        if raiz is None:
            return
        if resultado is None:
            resultado = []
        if eh_binaria(raiz): 
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
        self.reset_graph()
        InterfaceArvore.path_counter = 0

        altura = calcular_altura(self.tree)
        n_nos = contar_nos(self.tree)

        texto = f"A árvore possui {n_nos} nós,\ne tem altura {altura}."
        self.label.config(text=texto)

    def exibir_tipo(self):
        self.reset_graph()
        InterfaceArvore.path_counter = 0

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
        if node is None:
            return
        # Desenha linhas para nós filhos
        for i, child in enumerate(node.filhos):
            if child is not None: 
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


def main():
    # Árvore de teste (alterar árvore aqui)
    root = teste1()
    #root = teste2()
    #root = teste3()
    #root = teste4()
    #root = teste5()
    #root = teste6()
    #root = teste7()
    #root = teste8()

    # Carregar / Abrir interface gráfica
    try:
        app = InterfaceArvore(root)
        app.mainloop()
    except Exception as e:
        print(f"\nAlgo deu errado: {str(e)}")


if __name__ == "__main__":
    main()