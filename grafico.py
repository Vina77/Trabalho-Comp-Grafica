import pandas as pd
import matplotlib.pyplot as plt
from local import local

#Chama a classe "local" para achar o nome da planilha
arquivo = local()

#Le a planilha
df_arquivo = pd.read_excel(arquivo)

#Executa a planilha e exibe um grafica de barra
df_arquivo.plot(kind='bar')
plt.show()

