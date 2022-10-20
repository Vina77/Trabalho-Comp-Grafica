import os

def trantamento_texto(texto):
    numeros=['0','1','2','3','4','5','6','7','8','9']
    add_numeros=[]
    add_Letras=[]
    
    with open("valores_temp.txt", "w") as arquivo:
        arquivo.write(texto)
        
    
    with open("valores_temp.txt", "r") as arquivo:
        arq=arquivo.read()
    for array in arq.splitlines():
        array=array.split(' ')
        if array[0]=='0'or array[0]=='1'or array[0]=='2'or array[0]=='3'or array[0]=='4' or array[0]=='5' or array[0]=='6' or array[0]=='7' or array[0]=='8' or array[0]== '9':
            add_numeros.append(array[0])
        else:
            add_Letras.append(array[0])
                    
    os.remove("valores_temp.txt")
    print(add_Letras)
  
    
  
            
