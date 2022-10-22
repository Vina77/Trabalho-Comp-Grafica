import os

from numpy import append


def tratamento_texto(texto,textolista):
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
    list_texto=[textolista]
    tratado=[]
    
    for palavras in range(len(list_texto)):
        tratando=list_texto[palavras]                       #remover impurezas que acompanham os numeros
        for x in range(0,len(add_Letras)):
            tratando=tratando.replace(add_Letras[x],"")
            tratado.append(tratando)
   
    for x in add_Letras:
        print(x)           