import os 

def local():
   
    #pasta local onde os arquivos imagens serão salvos.
    #retorna o endereço completo da imagem
    list=[]
    path = (r"C:\Users")
    dir_list = os.listdir(path) 
    
    print("Qual é o seu usuario? ", path, " :")  
    list.append(dir_list)
    for x in list:
        cont=len(x)
        for i in range(cont):
            print(i,"-",x[i])
    
            
    user=int(input("Digite o numero: "))
    for x in list:
       print(x[user])
    
      
       
local()