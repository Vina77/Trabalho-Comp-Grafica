import cv2 as cv
import pytesseract as ts
import local
def leitura():
    #caminho_imagem=local()
    imagem=cv.imread(caminho_imagem)                     #leitura da imagem  


    caminho=(r'C:\Users\Vivo\AppData\Local\Tesseract-OCR')
    ts.pytesseract.tesseract_cmd = (caminho + r'\tesseract.exe')                    #tessaract serve para transformar a imagem em texto
    texto=ts.image_to_string(imagem)
    print(texto)                                                                
    
    #sugestão varrer leitura no texto gerado, se encontrar numeros separas este numeros e se tipos (reais, percento e etc)
    pass


    
    

    
    
    



