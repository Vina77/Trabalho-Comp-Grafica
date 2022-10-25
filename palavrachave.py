import pandas as pd
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
    if quantidade>0:                                             #caso deseja digitar as palavras chaves                       
        linha=[]    
        opcao="nao" 
        print("Digite as palavras chave que estão na imagem do mesmo formato")
        for x in range(0, quantidade):
            print("Deseja abrir a imagem? ")
            opcao=input()                                     #o usuario pode optar abrir a imagem para vizualizar as palavras 
            if opcao=="sim" or opcao=="s":
                cv.imshow("analise",analise)
                cv.waitKey(0)
            print("Digite as palavras chave que estão na imagem do mesmo formato")
            palavra=input()
            linha.append(palavra)                       #adicona na lista as palavras digitadas
        
        posicao_palavra_texto=[]
        posicao_numero_correspondente=[]
        
        for palavrachave in range(len(linha)):
            for palavra in texto:
                for x in range(len(palavra)):                #procura a palavra digitada e retorna a posição dela
                    if linha[palavrachave]==palavra[x]:
                        posicao_palavra_texto.append(x)
                        
        
        for compara in texto:
            for x in range(len(compara)):
                for y in numeros:
                    if compara[x]==y:                               #vai pegar todos os numeros do texto e suas posições no texto
                        posicao_numero_correspondente.append(x)
                                        
              
        
        tabela['palavra']=linha
        tabela['correspondentes']=0
        
        posicao_do_valor=[]
        
        for posi in range(0,len(posicao_palavra_texto)): 
            tam=len(posicao_numero_correspondente)-1
            aux=posicao_numero_correspondente[tam]
            for y in range(0,len(posicao_numero_correspondente)):
                comp=posicao_numero_correspondente[y]                   #vai verificar o numero mais perto da palavra digitada
                pos_val=posicao_palavra_texto[posi]   
                if comp>pos_val: 
                    aux2=comp
                    if aux>aux2:
                        aux=aux2
                        posicao_do_valor.append(aux2)
                    
                    
        numero_table=[]
        for numero in texto:
            for nums in range(len(numero)):
                for x in posicao_do_valor:                      #pega os numeros mais perto das palavras chaves e adiciona na lista
                    if x==nums:
                        numero_table.append(numero[nums])     
                            
        for x in range(len(linha)):
            for y in range(len(numero_table)):          #cria a planilha com as palavras e seus numeros correspondentes                                                 
                tabela.iloc[y,1]=numero_table[y]
        
                  
        
                
        tabela.to_excel(r'palavras_chave.xlsx')
        
        return(tabela)
                
    elif quantidade==0:
            tabela['numeros']=numeros                       #se o usuario optar por não usar palavras chaves cria uma planilha só com dados numericos
            tabela.to_excel(r'palavras_chave.xlsx')

            return(tabela)
    
    
    
