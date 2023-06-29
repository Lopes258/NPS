
import pandas as pd
import NPS_Googledrive


class Feedback:
    def __init__(self, nota, produto, tipo, Analista):
        self.nota = nota
        self.produto = produto
        self.tipo = tipo
        self.Analista = Analista

class AnalisadorFeedback:
    def __init__(self,feedbacks):
        self.feedbacks = feedbacks

    def calcular_nps(self):
        detratores = sum([1 for feedbacks in self.feedbacks if feedbacks.nota <= 6])
        promotores = sum([1 for feedbacks in self.feedbacks if feedbacks.nota >= 9])
        
        return (promotores - detratores) / len(self.feedbacks) * 100  
    

dados = pd.read_csv("../NPS/NPSDADOS.csv", delimiter =';')

feedbacks = [Feedback(linha['nota'], linha['produto'], linha['tipo'], linha['Analista'])  for i, linha in dados.iterrows()]

analisador = AnalisadorFeedback(feedbacks)
nps = analisador.calcular_nps()

print(nps)
