import cv2 as cv
import pytesseract as ts
from local import local
from tratamento_de_texto import trantamento_texto

def leitura():
    caminho_imagem=local()
    imagem=cv.imread(caminho_imagem)                     #leitura da imagem  
    
    gray_image = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)  
    #metodo para transformar uma imagem colorida em preto e branco   
    

    caminho=(r'C:\Users\Vivo\AppData\Local\Tesseract-OCR')
    ts.pytesseract.tesseract_cmd = (caminho + r'\tesseract.exe')    #tessaract serve para transformar a imagem em texto
    texto=ts.image_to_string(gray_image)
    
                                                                   
    trantamento_texto(texto)
    