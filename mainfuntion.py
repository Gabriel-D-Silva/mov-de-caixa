def pegarTexto(imagem):
    import pytesseract
    from os import path

    # Inicializa o Tesseract
    pytesseract.pytesseract.tesseract_cmd = path.join((path.dirname(__file__), "dependencies", "Tesseract-OCR", "tesseract.exe"))
    # Extrai o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang="por")

    return texto

def confirmarTexto(root):
    import tkinter as tk
    from tkinter import messagebox, filedialog
    from Convert import converterPDFS
    from rename_pastas import renomear_pastas_inicio, renomear_pastas_fim
    import os

    dados = {}
    
    messagebox.showinfo("Instrução", "Coloque o caminho da pasta como foi mostrado")
    path = filedialog.askdirectory()

    ####### VERIFICA SE A ESTRUTURA DE PASTA ESTA CORRETA

    renomear_pastas_inicio(path)

    pastas = ["ENTRADA", "SAÍDA"]

    pastaExiste = True

    for pasta in pastas:
        for i in range(1,13):
            if i < 10:
                if os.path.isdir(f"{path}\\{pasta}\\0{i}"):
                    pass
                else:
                    pastaExiste = False
            else:
                if os.path.isdir(f"{path}\\{pasta}\\{i}"):
                    pass
                else:
                    pastaExiste = False

    if pastaExiste == False:
        messagebox.showerror("Erro", "A pasta não está organizada devidamente na estrutura mostrada, organize ela")
        return 0

    renomear_pastas_fim(path)

    def bloquearFechamento():
        messagebox.showwarning("Ação Bloqueada", "Você não pode fechar esta janela.")

    ##### CRIA A PASTA QUE O APLICATIVO VAI USAR PARA COISAR

    messagebox.showinfo("Sucesso", "Aguarde alguns minutos pacientemente")

    converterPDFS(path)

    print("FEITO!")

    #### CRIA A JANELA, A CADA BOLETO PARA SER CONFIRMADO, UMA JANELA NOVA DEVE SER CRIADA

    janela = tk.Toplevel()

    # Manter a janela no topo
    janela.transient(root)
    janela.attributes("-topmost", True)

    janela.protocol("WM_DELETE_WINDOW", bloquearFechamento)


