import os

def trantamento_texto(texto):
    
    with open("valores_temp.txt", "w") as arquivo:
        arquivo.write(texto)
        
    
    with open("valores_temp.txt", "r") as arquivo:
        arq=arquivo.read()
    print(arq)
    
    
    
    """
    def etc():
    path = "diretorio"`
    dir = os.listdir(path)              #excuir arquivo temporario após pegar seus dados
    for file in dir:
        if file == "arquivo.txt":
            os.remove(file)"""
            
