def criarJanela(arquivo, root):
    import tkinter as tk
    from tkinter import messagebox
    from catchtext import pegarData, pegarNF, pegarTitulo, pegarValor

    def bloquearFechamento():
        messagebox.showwarning("Ação Bloqueada", "Você não pode fechar esta janela.")
    
    # Cria uma janela toplevel
    janela = tk.Toplevel()

    # Mantem a janela no topo
    janela.transient(root)
    janela.attributes("-topmost", True)
    janela.protocol("WM_DELETE_WINDOW", bloquearFechamento)

    # Cria o botão para fechar a janela toplevel
    botao_fechar = tk.Button(janela, text="Fechar", command=janela.destroy)
    botao_fechar.pack(pady=20)

    pegarTitulo(arquivo)
    pegarValor(arquivo)
    pegarData(arquivo)
    pegarNF(arquivo)

    print("----------------------------------------------------------------------------------------------")
    
    root.wait_window(janela)