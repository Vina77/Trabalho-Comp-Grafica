import pandas as pd
import numpy as np
import cv2 as cv

def palavra_chav(texto,numeros,imagem,bouding_boxes,nums):
    imH, imW,_=imagem.shape
    for boxes in bouding_boxes.splitlines():
        boxes=boxes.split(' ')
        for tam in range(len(nums)):
            if boxes[0]==nums[tam]:        #esse metodo faz com que apareça blocos nos numeros da imagem
                num,x,y,w,h=boxes[0],int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])        
                analise=cv.rectangle(imagem,(x,imH-y),(w,imH-h),(0,0,255),1)
   
    
    tabela=pd.DataFrame()
    
    print("Quantas palavras deseja digitar: ")
    quantidade=int(input())
    if quantidade>0:
        linha=[]    
        opcao="nao"
        print("Digite as palavras chave que estão na imagem do mesmo formato")
        for x in range(0, quantidade):
            print("Deseja abrir a imagem? ")
            opcao=input()
            if opcao=="sim" or opcao=="s":
                cv.imshow("analise",analise)
                cv.waitKey(0)
            print("Digite as palavras chave que estão na imagem do mesmo formato")
            palavra=input()
            linha.append(palavra)
        
        posicao_palavra_texto=[]
        posicao_palavra_linha=[]
        posicao_numero_correspondente=[]
        
        for palavrachave in range(len(linha)):
            for palavra in texto:
                for x in range(len(palavra)):
                    if linha[palavrachave]==palavra[x]:
                        posicao_palavra_texto.append(x)
                        posicao_palavra_linha.append(palavrachave)
        
        for compara in texto:
            for x in range(len(compara)):
                for y in numeros:
                    if compara[x]==y:
                        posicao_numero_correspondente.append(x)
                                        
              
        
        tabela['palavra']=linha
        tabela['correspondentes']=0
        
        for x in range(len(posicao_numero_correspondente)):
            for y in range(len(posicao_palavra_texto)):
                comp=0
                tam=len(posicao_numero_correspondente)
                compara=int(posicao_numero_correspondente[x])
                aux=int(posicao_numero_correspondente[tam-tam+comp])
                if aux==compara
                print(compara," - ",aux)
        
        
        print(posicao_palavra_texto)
        print(posicao_palavra_linha)
        print(posicao_numero_correspondente)
                      
        
                
        tabela.to_excel(r'palavras_chave.xlsx')        
    elif quantidade==0:
            tabela['numeros']=numeros
            tabela.to_excel(r'palavras_chave.xlsx')
    
    #else:
        #ecessão()
        
    planilha=(r'palavras_chave.xlsx')
    
    lista_contem_texto=[]
    
