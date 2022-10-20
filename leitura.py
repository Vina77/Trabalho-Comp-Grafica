import cv2 as cv
import pytesseract as ts
from local import local
from tratamento_de_texto import trantamento_texto
import os

def leitura_de_imagem():
    caminho_imagem=local()
    imagem=cv.imread(caminho_imagem)    #leitura da imagem
    altura, largura = imagem.shape[0:2] 
    if  altura>500 and largura>500:
        imagem=cv.resize(imagem,(0,0),fx=0.5,fy=0.5)        #verificação do tamanho da imagem para redimensionamento
                                                
    imagem_cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)  #metodo para transfiormar uma imagem colorida em preto e branco   
    
    imagem_board=cv.Laplacian(imagem_cinza,cv.CV_8U)       #metodo de detecção de bordas
    
    
    cv.imshow("Live", imagem_board)

    key = cv.waitKey(0) 
    cv.destroyAllWindows()  
    
    
    
    caminho=(r'C:\Users\Vivo\AppData\Local\Tesseract-OCR')
    ts.pytesseract.tesseract_cmd = (caminho + r'\tesseract.exe')    #tessaract serve para transformar a imagem em texto
    teste_texto=ts.image_to_string(imagem)
    with open("texto_temp.txt", "w") as arquivo:
        arquivo.write(teste_texto)
    retorno=os.path.getsize("texto_temp.txt")
    print(retorno)
    
    if retorno==0:
        os.remove("texto_temp.txt")
        texto=ts.image_to_boxes(imagem_board)
        
    else:
        texto=ts.image_to_boxes(imagem_cinza)
        
    
                                                                   
    trantamento_texto(texto)
    