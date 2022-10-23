import pandas as pd
import numpy as np

def palavra_chav(texto,numeros):
    tabela=pd.DataFrame()
    print("Quantas palavras deseja digitar: ")
    quantidade=int(input())
    linha=[]    
    
    for x in range(0, quantidade):
        print("digite as palavras chave")
        palavra=input()
        print("\n")
        linha.append(palavra)
    
    tabela['palavra']=linha
    tabela.to_excel(r'palavras_chave.xlsx')
    
    planilha=(r'palavras_chave.xlsx')
    
    lista_contem_texto=[]
    
