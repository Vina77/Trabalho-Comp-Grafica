import os

from palavrachave import palavra_chav


def tratamento_texto(texto,textolista,imagem):
    add_numeros=[]                      #lista para separação de letras e numeros 
    add_Letras=[" ","{"," ","","}","_","'"]

    
    with open("valores_temp.txt", "w") as arquivo:
        arquivo.write(texto)                                #cria um arquivo tmp para tratar
        
    
    with open("valores_temp.txt", "r") as arquivo:
        arq=arquivo.read()                                  #leitura do arquivo
    
    for array in arq.splitlines():
        array=array.split(' ')         #separa e cria um array com os caracteres encontrados no texto, separação de letras e numeros
        if array[0]=='0'or array[0]=='1'or array[0]=='2'or array[0]=='3'or array[0]=='4' or array[0]=='5' or array[0]=='6' or array[0]=='7' or array[0]=='8' or array[0]== '9':
            add_numeros.append(array[0])
            
        else:
            add_Letras.append(array[0])
        
    os.remove("valores_temp.txt")           #apaga o arquivo         
    
    list_texto=[]
    list_numero=[]
    palavra=textolista.split()
    
    list_texto.append(palavra)
    
    num_float=[]
    floatnum=0.0
    for nums in range(100000):
        floatnum+=0.01
        conv0=round(floatnum,2)                                 #cirando lista com possiveis numeros com virgula
        conv=str(conv0).replace(".",",")
        num_float.append(conv)
    
    for x in palavra:
        p=x
        for y in range(len(num_float)):                             #adicionando a lista numeros com virgula
            if p==num_float[y] or p==num_float[y]+"%":
                list_numero.append(p)
                
    for x in palavra:
        p=x                                 #captura numeros inteiros
        if p.isdigit():
            list_numero.append(p)
    
    list_possible_nums=[]
    for x in range(10000):
        conv=str(x)
        list_possible_nums.append(conv)
    
    for x in palavra:
        p=x
        for y in range(len(list_possible_nums)):
            if p==list_possible_nums[y] or p==list_possible_nums[y]+"." or p==list_possible_nums[y]+"%" or p==list_possible_nums[y]+",":
                list_numero.append(p)
              
    
    
     
    palavra_chav(list_texto,list_numero,imagem,texto,add_numeros)
                
    
        
        
                 
    
  
              