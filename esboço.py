import cv2
import pytesseract
from pdf2image import convert_from_path

# PROBLEMA 1: CRIAR PASTAS PARA TODAS AS ENTRADAS E SAIDAS NA PASTA 'CONVERTIDOS' (que ficará na pasta script), PARA QUE, QUANDO O PROGRAMA FOR FAZER A CONVERSÃO, ELE TENHA ONDE COLOCAR-LOS DE FORMA ORGANIZADA
# PROBLEMA 2: CONTVERER DE FATO TODOS OS COMPROVANTES DE PAGAMENTOS PARA IMAGENS E ORGANIZA-LOS DEVIDAMENTE NA PAGINA /script/convertidos
# PROBLEMA 3: PARA CADA COMPROVANTE DE PAGAMENTO, PUXAR O TEXTO CONTIDO E LOCALIZAR ONDE SE ENCONTRA O VALOR EM REAIS
# PROBLEMA 4: CRIAR UMA PLANILHA EXCEL COM A ESTRUTURA PRONTA PARA RECEBER OS DADOS DE ENTRADA E SAÍDA
# PROBLEMA 5: DEPENDENDO DA PASTA ONDE O COMPROVANTE SE ENCONTRA (entrada ou saída), PEGAR ESSE VALOR E COLOCA-LO NO SEU DEVIDO LUGAR (mês) NA PLANILHA EXCEL 
# PROBLEMA 6: SINTETIZAR TUDO ISSO NUM APP DESKTOP COM INTERFACE DE USUARIO PARA USO NOS ANOS SEGUINTES

## PROBLEMA N° 1
# Converter PDF para uma lista de imagens
images = convert_from_path(r'C:\Users\JOEL\Desktop\automacao_jc\2024\ENTRADA\02-FEV\COMPROVANTE DE PAGAMENTO 2 .1.pdf', poppler_path=r"C:\\Users\\JOEL\\Desktop\\automacao_jc\\script\\poppler-24.08.0\\Library\\bin")
# Salvar as imagens
for i, image in enumerate(images):
    image.save(f'C:\\Users\\JOEL\\Desktop\\automacao_jc\\script\\convertidos\\pagina_{i}.png', 'PNG')

# PROBLEMA N° 2
# Abre a imagem numa variavel
imagem_teste = cv2.imread(r'C:\Users\JOEL\Desktop\automacao_jc\script\convertidos\pagina_0.png')
# Verifica se a imagem foi carregada
if imagem_teste is None:
    print("Erro: a imagem não foi carregada corretamente. Verifique o caminho do arquivo.")
else:
    print("Imagem carregada com sucesso.")

# PROBLEMA N° 3
# Inicializa o Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Extrai o texto da imagem
texto = pytesseract.image_to_string(imagem_teste, lang="por")

print(texto)
