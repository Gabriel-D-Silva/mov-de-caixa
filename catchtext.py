def pegarValor(imagem):
    import pytesseract
    import re

    # Extrai o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang="por")

    # Puxa a primeira série de numeros depois da string "VALOR TOTAL" aparecer
    palavra_chave = "VALOR TOTAL"

    padrao = rf"{palavra_chave}.*?(\d+[\.,]?\d*)"

    numero = re.search(padrao, texto.upper(), re.DOTALL)

    if numero is not None:
        valor = numero.group(1).strip()
        print("Valor encontrado: R$", valor)
        return valor
    else:
        print("Valor não encontrado")
        return ""
    
def pegarTitulo(imagem):
    import pytesseract
    import re

    # Extrai o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang="por")

    palavra_chave_inicio = "RECEBEMOS DE"
    palavra_chave_fim = "OS"

    padrao = rf"{palavra_chave_inicio}(.*?){palavra_chave_fim}"

    titulo = re.search(padrao, texto.upper(), re.DOTALL)

    if titulo is not None:
        valor = titulo.group(1).strip()
        print("Titulo encontrado: ", valor)
        return valor
    else:
        print("Titulo não encontrado")
        return ""
    
def pegarData(imagem):
    import pytesseract
    import re

    # Extrai o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang="por")

    # Define a palavra-chave
    palavra_chave = "DATA DA"

    # Padrão para capturar a data
    padrao = rf"{palavra_chave}.*?(\d{{2}}/\d{{2}}/\d{{4}})"

    data = re.search(padrao, texto, re.DOTALL)

    if data is not None:
        valor_data = data.group(1).strip()
        print("Data encontrada:", valor_data)
        return valor_data
    else:
        print("Data não encontrada")
        return ""
    
def pegarNF(imagem):
    import pytesseract
    import re

    # Extrai o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang="por")

    # Define a palavra-chave
    palavra_chave = "N°"

    # Padrão para capturar a data
    padrao = rf"{palavra_chave}[\s:.]*(\d{{1,3}}(?:\.\d{{3}})*|\d{{3,9}})"

    nf = re.search(padrao, texto, re.DOTALL)

    if nf is not None:
        valor_data = nf.group(1).strip()
        print("NF encontrada:", valor_data)
        return valor_data
    else:
        print("NF não encontrada")
        return ""