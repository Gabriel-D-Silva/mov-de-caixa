def converterPDFS(alvo_dir):
    import os
    import locale
    from datetime import date
    from pdf2image import convert_from_path
    from rename_pastas import renomear_pastas_fim, renomear_pastas_inicio
    from list_pdfs import listar_pdfs

    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

    # CAMINHO DA PASTA
    script_dir = os.path.dirname(__file__)
    poppler_dir = os.path.join(script_dir, "dependencies", "poppler-24.08.0", "Library", "bin")
    convertidos_dir = os.path.join(script_dir, "convertidos")

    pastas = ["ENTRADA", "SAÍDA", "EXTRATOS BANCÁRIOS"]

    # CRIAÇÃO DAS PASTAS
    os.mkdir(f'{convertidos_dir}\\{date.today()}')
    for pasta in pastas:
        os.mkdir(f'{convertidos_dir}\\{date.today()}\\{pasta}')
        if pasta != pastas[2]:
            for i in range(1 ,13):
                if i < 10:
                    os.mkdir(f'{convertidos_dir}\\{date.today()}\\{pasta}\\0{i}')
                else:
                    os.mkdir(f'{convertidos_dir}\\{date.today()}\\{pasta}\\{i}')
        else:
            pass

    renomear_pastas_inicio(alvo_dir)

    # CONVERSÃO DE PDF PARA IMAGENS LEGIVEIS PELO TESSERACT
    for pasta in pastas:
        if pasta != pastas[2]:
            for i in range(1, 13):
                if i < 10:
                    atual_dir = os.path.join(alvo_dir, f"{pasta}", f"0{i}")
                else: 
                    atual_dir = os.path.join(alvo_dir, f"{pasta}", f"{i}")
                arquivos = listar_pdfs(atual_dir)
                for arquivo in arquivos:
                    if i < 10:
                        imagem = convert_from_path(arquivo, poppler_path=f"{poppler_dir}")
                        imagem[0].save(f"{convertidos_dir}\\{date.today()}\\{pasta}\\0{i}\\{os.path.basename(arquivo)}.png", "PNG")
                    else:
                        imagem = convert_from_path(arquivo, poppler_path=f"{poppler_dir}")
                        imagem[0].save(f"{convertidos_dir}\\{date.today()}\\{pasta}\\{i}\\{os.path.basename(arquivo)}.png", "PNG")
        else:
            atual_dir = os.path.join(alvo_dir, f"{pasta}")
            arquivos = listar_pdfs(atual_dir)

            for arquivo in arquivos:
                imagem = convert_from_path(arquivo, poppler_path=f"{poppler_dir}")
                for j, img in enumerate(imagem):
                    img.save(f"{convertidos_dir}\\{date.today()}\\{pasta}\\{os.path.basename(arquivo)}_pag{j}.png", "PNG")

    renomear_pastas_fim(alvo_dir)