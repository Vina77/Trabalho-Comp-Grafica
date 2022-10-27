import pandas as pd
import matplotlib.pyplot as plt
from local import local

def grafico():
    #Chama a classe "local" para achar o nome da planilha
    arquivo = local()

    #Le a planilha
    df_arquivo = pd.read_excel(arquivo)

    aux = int(input("Escolha 1 para grafico em barra ou 2 para o grafico em pizza: "))
    if aux == 1:
        #Define o nome do eixo X
        eixoX = input("Coloque o nome para o eixo X: ")
        print("Nome do eixo X: " + eixoX)

        #Define o nome do eixo Y
        eixoY = input("Coloque o nome para o eixo Y: ")
        print("Nome do eixo Y: " + eixoY)

        #Exibe um grafico de barra
        df_arquivo.plot(kind='bar')
        plt.xlabel(eixoX)
        plt.ylabel(eixoY)
        plt.show()

    elif aux == 2:
        #Define a coluna que sera usada para construir o grafico
        dadoGraf = input("Coloque a coluna do dado para construir o gráfico: ")
        print("A coluna é: " + dadoGraf)
        
        #Define a coluna com os nomes dos dados acima
        labelName = input("Coloque a coluna com os respectivos nomes dos dados escolhidos: ")
        print("A coluna é: " + labelName)

        #Exibe um grafico de pizza
        plt.pie(df_arquivo[dadoGraf], labels = df_arquivo[labelName])
        plt.show()
    else:
        print("Opção invalida")

def verifica():
    #Pergunta se o usuario gostario de construir uma grafico
    aux = input("Coloque 1 para construir o grafico ou qualquer outra tecla para finalizar o programa")
    if aux == 1:
        grafico()
    else:
        print("Fim do programa")        
