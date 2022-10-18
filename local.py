import os 

def local(): 
    #pasta local onde os arquivos imagens serão salvos.
    #retorna o endereço completo da imagem
    list=[]
    path = (r"C:\Users")
    dir_list = os.listdir(path) 
    
    print("Qual é o seu usuario? ", path, " :")  
    list.append(dir_list)
    for x in list:                                  #da uma lista de usuarios que tem na maquina
        cont=len(x)
        for i in range(cont):
            print(i,"-",x[i])
    
            
    user=int(input("Digite o numero: "))
    usuario=path+"\\"  #caso windowns 
    for x in list:
       usuario=usuario+x[user]
    
    usuario=usuario+"\Downloads"                #apos o usuario selecionado vai direto para pasta downloads
    
    arquivo=os.listdir(usuario)
    list.clear()
    print (list)
    list.append(arquivo)
    
    for x in list:
        cont=len(x)
        for i in range(cont):                                       #lista de arquivos e diretorios na pasta downloadsé
            print(i,"-",x[i])
    
    arq=int(input("Digite o numero do arquivo: "))
    for x in list:
        local_imagem=usuario+"\\"+x[arq]  #caso windowns 
        
    return local_imagem             #retorna o local onde a imagem a ser reconhecida
