import pandas as pd
import NPS_Googledrive
import CalculoNPS
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# Definição das constantes que usaremos para visualizar o NPS
NPS_ZONAS =   ['Crítico', 'Aperfeiçoamento', 'Qualidade', 'Excelência']
NPS_VALORES = [-100, 0, 50, 75, 100]
NPS_CORES =   ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']

#Import de variavel de outro arquivo
nps = CalculoNPS.nps

# TODO: Criar um gráfico usando "matplotlib" para visualizar o NPS que calculamos no Dia 1!
def criar_grafico_nps(nps):
    fig, ax = plt.subplots(figsize=(10,2))

    for i, zona in enumerate(NPS_ZONAS):
        ax.barh([0], width=NPS_VALORES[i+1]-NPS_VALORES[i], left=NPS_VALORES[i], color=NPS_CORES[i]) # para criar o grafico

    ax.barh([0], width=1, left=nps, color = 'black') # para demonstrar o valor de nps no grafico
    ax.set_yticks([]) # para remover o eixo Y
    ax.set_xlim(-100,100) #para determinar o incio e o fim do grafico
    ax.set_xticks(NPS_VALORES) #para determinar o eixo X

    plt.text(nps, 0, f'{nps:.2f}', ha='center', va='center', color='white', bbox=dict(facecolor='black'))

    patches = [mpatches.Patch(color=NPS_CORES[i], label = NPS_ZONAS[i]) for i in range (len(NPS_ZONAS))]
    plt.legend(handles=patches, bbox_to_anchor=(1,1))
    plt.title(label= 'Nota de NPS')

    plt.show()

criar_grafico_nps(nps)