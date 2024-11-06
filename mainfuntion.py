def confirmarTexto(root):
    import tkinter as tk
    from tkinter import messagebox, filedialog
    from Convert import converterPDFS
    from rename_pastas import renomear_pastas_inicio, renomear_pastas_fim
    from verif_window import criarJanela
    import os
    from datetime import date

    filepath = os.path.dirname(__file__)
    
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

    ##### CRIA A PASTA QUE O APLICATIVO VAI USAR PARA COISAR

    messagebox.showinfo("Sucesso", "Aguarde alguns minutos pacientemente")

    converterPDFS(path)

    messagebox.showinfo("Sucesso", "O aplicativo vai conferir os valores dos documentos, verifique se os valores estão corretos")

    ### LOOP PARA PERCORRER TODOS OS ARQUIVOS CONVERTIDOS E CRIAR UMA JANELA DE CONFIRMAÇÃO PRA
    ### CADA CABRUNCO FEIO DESSE

    convertidos = os.path.join(filepath, "convertidos", f"{date.today()}")

    import pytesseract

    # Inicializa o Tesseract
    tesseract_path = os.path.join(f"{os.path.dirname(__file__)}", "dependencies", "Tesseract-OCR", "tesseract.exe")
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    for pasta in pastas:
        for i in range(1,13):
            if i < 10:
                planilha = {"DATA":[], "HISTÓRICO":[1], "NF/RECIBO":[], "ENTRADA":[1], "SAÍDA":[1]}
                arquivos = os.listdir(f"{convertidos}\\{pasta}\\0{i}")
                for arquivo in arquivos:
                    arquivo_path = os.path.join(convertidos, f"{pasta}", f"0{i}", arquivo)
                    dados = criarJanela(arquivo_path, root)

            else:
                arquivos = os.listdir(f"{convertidos}\\{pasta}\\{i}")
                for arquivo in arquivos:
                    arquivo_path = os.path.join(convertidos, f"{pasta}", f"{i}", arquivo)
                    criarJanela(arquivo_path, root)



