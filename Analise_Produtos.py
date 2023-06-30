import os
import openai
import CalculoNPS
import NPS_Googledrive
import pandas as pd


openai.api_key = API_KEY



feedbacks = CalculoNPS.feedbacks
dados = pd.read_csv("../NPS/NPSDADOS.csv", delimiter =';')


def  analisar_produtos(analise):

    comentarios_formatados = "\n".join([f"- {feedbacks.nota}" for feedbacks in analise])
    prompt = f"Separe os produtos por nps:\n{comentarios_formatados}"

    respostaAPI = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=20,
        messages=[
            {"role": "system", 
             "content": "Você é um modelo de análises de comentários."
             },
            {"role": "user", 
             "content": prompt
             }
  ]
)
    
    return respostaAPI.choices[0].message.content


insigths = analisar_produtos(feedbacks)
print(insigths)