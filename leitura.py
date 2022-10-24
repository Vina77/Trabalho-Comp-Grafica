import cv2 as cv
import pytesseract as ts
from local import local

from tratamentos import  tratamento_texto
import os

def leitura_de_imagem():
    caminho_imagem=local()
    imagem=cv.imread(caminho_imagem)    #leitura da imagem
    altura, largura = imagem.shape[0:2] 
    proporcao=float(altura/largura)
    
    if  proporcao<1:
        imagem=cv.resize(imagem,(0,0),fx=1.2,fy=1.2)        #verificação do tamanho da imagem para redimensionamento
                                           
    
    imagem_cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)  #metodo para transfiormar uma imagem colorida em preto e branco   
    
    imagem_board=cv.Laplacian(imagem_cinza,cv.CV_8U)       #metodo de detecção de bordas
    
    
    caminho=(r'C:\Users\Vivo\AppData\Local\Tesseract-OCR')
    ts.pytesseract.tesseract_cmd = (caminho + r'\tesseract.exe')    #tessaract serve para transformar a imagem em texto
    teste_texto=ts.image_to_string(imagem,lang='por')
    
    with open("texto_temp.txt", "w") as arquivo:
        arquivo.write(teste_texto)                  #teste para verificar se ele conseguiu ler alguma coisa
    retorno=os.path.getsize("texto_temp.txt")
    
    
    if retorno==0:
        os.remove("texto_temp.txt")
        texto=ts.image_to_boxes(imagem_board,lang='por')           #caso for zero ele vai tentar verificar pelas bordas
        
    else:
        os.remove("texto_temp.txt")
        texto=ts.image_to_boxes(imagem_cinza,lang='por')           #se não uma imagem preto e branco
       
                                                                   
    tratamento_texto(texto,teste_texto,imagem)
    