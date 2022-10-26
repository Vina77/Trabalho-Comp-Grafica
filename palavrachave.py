import pandas as pd
import cv2 as cv
import re
from grafico import grafico 

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
        tabela["convertido"]=0
        
        posicao_do_valor=[]
        
        for posi in range(0,len(posicao_palavra_texto)): 
            tam=len(posicao_numero_correspondente)
            tam=tam-1
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
        
        
        #pegar numeros em numero_table e transoformar em numeros
        
        
        tipos_numero=["1","2","3","4","5","6","7","8","9","0"] 
        cont=0 
        chars=[]                  
        #cria a planilha com as palavras e seus numeros correspondentes
        for x in range(len(linha)):
            for y in range(len(numero_table)):
                cont=0
                troca=numero_table[y]            #for para trocar para numeros reais
                for z in range(len(troca)):
                    tam=len(troca)-1
                    tam2=len(troca)
                    if troca[z]=="," or troca[z]==".":                  #verifica se tem . ou ,
                        cont=0                                  
                        for num in tipos_numero:                #caso float
                            if troca[tam]==num:
                                troca=troca.replace(",",".")
                                novo_numero=float(troca)
                                numero_table[y]=novo_numero
                            elif troca[tam]=="," or troca[tam]==".":
                                novo_numero=re.sub('[.,!]', '',troca)
                                novo_numero=int(novo_numero)
                                numero_table[y]=novo_numero
                            elif troca[tam]=="%" and troca[tam-1]==num:
                                novo_numero=re.sub('[%]', '',troca) 
                                novo_numero=novo_numero.replace(",",".")      
                                novo_numero=float(novo_numero)
                                novo_numero=novo_numero/100
                                numero_table[y]=novo_numero
                    else:                               #caso inteiro          
                        for num in tipos_numero:
                            if num==troca[z]:
                                cont+=1
                                if cont==tam2:
                                    novo_numero=int(troca)
                                    numero_table[y]=novo_numero
                                    cont=0   
    
    
    
                                                     

        for x in range(len(linha)):
            for y in range(len(numero_table)):         
                novo_numero=int(numero_table[y])
                tabela.iloc[y,1]=numero_table[y]
                tabela.iloc[y,2]=novo_numero
                
        tabela.to_excel(r'palavras_chave.xlsx')
        grafico()
        return(tabela)
                
    elif quantidade==0:
        tipos_numero=["1","2","3","4","5","6","7","8","9","0"] 
        cont=0 
        
        for y in range(len(numeros)):
            cont=0
            troca=numeros[y]
            tam=len(numeros[y])
            tam=tam-1
            tam2=len(numeros[y])
            for z in range(len(troca)):                         #verifica se tem . ou ,
                if troca[z]=="," or troca[z]==".":
                    cont=0          
                    for num in tipos_numero:                         #caso float
                        if troca[tam]==num:
                            novo_numero=troca
                            novo_numero=novo_numero.replace(",",".")
                            novo_numero=float(novo_numero)
                            numeros[y]=novo_numero
                        elif troca[tam]=="," or troca[tam]==".":
                            novo_numero=re.sub('[.,!]', '',troca)
                            novo_numero=int(novo_numero)
                            numeros[y]=novo_numero
                        elif troca[tam]=="%" and troca[tam-1]==num:
                            novo_numero=re.sub('[%]', '',troca) 
                            novo_numero=novo_numero.replace(",",".")      
                            novo_numero=float(novo_numero)
                            novo_numero=novo_numero/100
                            numeros[y]=novo_numero
                else:          
                    for num in tipos_numero:
                        if num==troca[z]:
                            cont+=1
                            if cont==tam2:
                                novo_numero=troca
                                novo_numero=int(novo_numero)
                                numeros[y]=novo_numero
                                cont=0
        

        tabela['Dados']="dados"
        tabela['numeros']=numeros   #se o usuario optar por não usar palavras chaves cria uma planilha só com dados numericos
        tabela["correspondentes"]=0
        
        for x in  range(len(numeros)):
            novo_numero=int(numeros[x])
            tabela.iloc[x,2]=novo_numero
        
        tabela.to_excel(r'palavras_chave.xlsx')
        
        grafico()
        return(tabela)
        
    
    
    
