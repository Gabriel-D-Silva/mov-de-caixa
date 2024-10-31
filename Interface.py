from os import mkdir
from datetime import date
import tkinter as tk
from tkinter import PhotoImage, filedialog, messagebox
from rename_pastas import renomear_pastas_fim
from mainfuntion import *

hoje = date.today()
pastas = ["ENTRADA", "SAÍDA", "EXTRATOS BANCÁRIOS"]

root = tk.Tk()

def criarPastaCaixa():
    diretorio = filedialog.askdirectory()
    if diretorio:
        try:
            mkdir(f"{diretorio}\\MOVIMENTO DE CAIXA {hoje.year}")
            for pasta in pastas:
                if pasta != pastas[2]:
                    mkdir(f"{diretorio}\\MOVIMENTO DE CAIXA {hoje.year}\\{pasta}")
                    for i in range(1,13):
                        if i < 10:
                            mkdir(f"{diretorio}\\MOVIMENTO DE CAIXA {hoje.year}\\{pasta}\\0{i}")
                        else:
                            mkdir(f"{diretorio}\\MOVIMENTO DE CAIXA {hoje.year}\\{pasta}\\{i}")
                else:
                    mkdir(f"{diretorio}\\MOVIMENTO DE CAIXA {hoje.year}\\{pasta}")
            renomear_pastas_fim(f"{diretorio}\\MOVIMENTO DE CAIXA {hoje.year}")
            messagebox.showinfo("Aviso", f"A pasta foi criada com sucesso no caminho \'{diretorio}\\MOVIMENTO DE CAIXA {hoje.year}\'")
        except FileExistsError:
            messagebox.showerror("Erro", "Esse caminho já possui uma pasta de movimento de caixa.")

t1 = "Antes de fazermos sua planilha, você deve organizar suas contas dentro de uma pasta com a estrutura abaixo, certifique-se de que suas contas já estão organizadas da forma abaixo, ou crie uma pasta e organize suas contas lá primeiro"
t2 = "Não possuo, quero criar uma pasta de contas"
t3 = "Já possuo uma, quero seleciona-la e fazer sua planilha"
print1 = PhotoImage(file="1.png")
print2 = PhotoImage(file="2.png")
warning = PhotoImage(file="warning.png")


frame_top = tk.Frame(root)
aviso = tk.Label(frame_top, text=t1, font=("Helvetica", 16, "bold"), wraplength=750, justify="left")
foto_warning = tk.Label(frame_top, image=warning, width=100, height=100)
aviso.pack(side='right', pady=10, padx=10, fill="both")
foto_warning.pack(side="left")
frame_top.pack()

frame_center = tk.Frame(root)
foto1 = tk.Label(frame_center, image=print1)
foto1.pack(side="left")
foto2 = tk.Label(frame_center, image=print2)
foto2.pack(side="right")
frame_center.pack(padx=10, pady=10)

frame_bottom = tk.Frame(root)
botao1 = tk.Button(frame_bottom, text=t2, command=criarPastaCaixa, 
    bg="#FFFF00", fg="black", font=("Helvetica", 12, "bold"), relief="raised", bd=3, padx=10, pady=5)
botao1.pack(side="left", padx=10, pady=20)
botao2 = tk.Button(frame_bottom, text=t3, command=lambda :confirmarTexto(root),
    bg="#4CAF50", fg="black", font=("Helvetica", 12, "bold"), relief="raised", bd=3, padx=10, pady=5)
botao2.pack(side="right", padx=10, pady=20)
frame_bottom.pack()

root.mainloop()