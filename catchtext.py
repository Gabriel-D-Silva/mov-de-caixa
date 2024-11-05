def pegarValor(imagem):
    import pytesseract
    from os import path
    import re

    # Inicializa o Tesseract
    tesseract_path = path.join(path.dirname(__file__), "dependencies", "Tesseract-OCR", "tesseract.exe")
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # Extrai o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang="por")

    # Puxa a primeira série de numeros depois da string "VALOR TOTAL" aparecer
    palavra_chave = "VALOR TOTAL"

    padrao = rf"{palavra_chave}.*?(\d+[\.,]?\d*)"

    numero = re.search(padrao, texto.upper(), re.DOTALL)

    if numero is not None:
        valor = numero.group(1).strip()
        print(texto)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Valor encontrado: R$", valor)
        print("----------------------------------------------------------------------------------------------------------------------")
        return valor
    else:
        print("Valor não encontrado")
        return ""