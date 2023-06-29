#Codigo para baixar a planilha de um drive para conseguir utilizar

import gdown
import pandas as pd

file_id = '1cSJFwGf-I5ku31DFwOEYIh79d56N9DZt'
gdown.download(f'https://drive.google.com/uc?id={file_id}', 'NPSDADOS.csv')

dados = pd.read_csv("../NPS/NPSDADOS.csv", delimiter =';')