import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas com Estatísticas")
        self.texto = tk.Text(root)
        self.texto.pack(expand=True, fill='both')
        self.iniciar_botoes()
        self.texto.config(bg="#002FA7", fg="white", font=("Arial", 14, "bold"))
        self.inicio = datetime.now()    # Inicializa a variável self.inicio

    def iniciar_botoes(self):
        s = ttk.Style()
        s.configure('my.TFrame', background='#002FA7', borderwidth=10, relief='flat', padding=10)
        frame_botoes = ttk.Frame(self.root, style='my.TFrame')
        frame_botoes.pack()
        
        botao_estatisticas = ttk.Button(frame_botoes, text="Estatísticas", command=self.calcular_estatisticas)
        botao_estatisticas.pack(side=tk.LEFT)
        
        botao_salvar = ttk.Button(frame_botoes, text="Salvar", command=self.salvar_arquivo)
        botao_salvar.pack(side=tk.LEFT)

        botao_abrir = ttk.Button(frame_botoes, text="Abrir", command=self.abrir_arquivo)
        botao_abrir.pack(side=tk.LEFT)

    def calcular_estatisticas(self):
        texto = self.texto.get("1.0", "end-1c")
        palavras = len(texto.split())
        caracteres = len(texto.replace(" ", ""))
        tempo_total = datetime.now() - self.inicio
        segundos_totais = tempo_total.total_seconds()
        palavras_por_segundo = palavras / segundos_totais if segundos_totais > 0 else 0
        teclas_por_segundo = caracteres / segundos_totais if segundos_totais > 0 else 0

        messagebox.showinfo("Estatísticas",
                            f"Palavras por segundo: {palavras_por_segundo:.2f}\n"
                            f"Teclas por segundo: {teclas_por_segundo:.2f}\n"
                            f"Tempo total no arquivo: {tempo_total}\n"
                            f"Tempo total escrevendo: {segundos_totais:.2f} segundos")

    def salvar_arquivo(self):
        texto = self.texto.get("1.0", "end-1c")
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])

        if file_path:
            with open(file_path, "w") as file:
                file.write(texto)

    def abrir_arquivo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

        if file_path:
            with open(file_path, "r") as file:
                texto = file.read()
                self.texto.delete("1.0", "end")
                self.texto.insert("1.0", texto)

if __name__ == "__main__":
    root = tk.Tk()
    bloco_de_notas = BlocoDeNotas(root)
    root.mainloop()
