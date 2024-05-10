import pandas as pd
import requests
import matplotlib.pyplot as plt 
# URLs da API
urls = [
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-01-01&dat_fim=2021-03-21&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-03-21&dat_fim=2021-06-21&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-06-21&dat_fim=2021-09-23&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-09-23&dat_fim=2021-12-21&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-01-01&dat_fim=2022-03-21&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-03-21&dat_fim=2022-06-21&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-06-21&dat_fim=2022-09-23&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-09-23&dat_fim=2022-12-21&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-01-01&dat_fim=2023-03-21&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-03-21&dat_fim=2023-06-21&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-06-21&dat_fim=2023-09-23&cod_areacarga=N',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-09-23&dat_fim=2023-12-21&cod_areacarga=N',
    
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-01-01&dat_fim=2021-03-21&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-03-21&dat_fim=2021-06-21&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-06-21&dat_fim=2021-09-23&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-09-23&dat_fim=2021-12-21&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-01-01&dat_fim=2022-03-21&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-03-21&dat_fim=2022-06-21&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-06-21&dat_fim=2022-09-23&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-09-23&dat_fim=2022-12-21&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-01-01&dat_fim=2023-03-21&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-03-21&dat_fim=2023-06-21&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-06-21&dat_fim=2023-09-23&cod_areacarga=NE',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-09-23&dat_fim=2023-12-21&cod_areacarga=NE',


    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-01-01&dat_fim=2021-03-21&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-03-21&dat_fim=2021-06-21&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-06-21&dat_fim=2021-09-23&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-09-23&dat_fim=2021-12-21&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-01-01&dat_fim=2022-03-21&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-03-21&dat_fim=2022-06-21&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-06-21&dat_fim=2022-09-23&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-09-23&dat_fim=2022-12-21&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-01-01&dat_fim=2023-03-21&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-03-21&dat_fim=2023-06-21&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-06-21&dat_fim=2023-09-23&cod_areacarga=S',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-09-23&dat_fim=2023-12-21&cod_areacarga=S',

    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-01-01&dat_fim=2021-03-21&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-03-21&dat_fim=2021-06-21&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-06-21&dat_fim=2021-09-23&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2021-09-23&dat_fim=2021-12-21&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-01-01&dat_fim=2022-03-21&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-03-21&dat_fim=2022-06-21&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-06-21&dat_fim=2022-09-23&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2022-09-23&dat_fim=2022-12-21&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-01-01&dat_fim=2023-03-21&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-03-21&dat_fim=2023-06-21&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-06-21&dat_fim=2023-09-23&cod_areacarga=SECO',
    'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2023-09-23&dat_fim=2023-12-21&cod_areacarga=SECO',
                                                                                                                     ]

# Lista para armazenar as médias
medias = []

# Loop sobre as URLs
for url in urls:     

# Fazer a solicitação HTTP à API
    response = requests.get(url)      
    data = response.json()

# Calculo de média a partir de um nome
    df = pd.DataFrame(data)
    media_val_cargaglobal = df['val_cargaglobal'].mean()
    medias.append(media_val_cargaglobal)

# Criação de nomemxlatura para divisão em .CSV
df_medias = pd.DataFrame({"API de Consulta": urls, "Media Por Consumo": medias,})

 # Exibir as médias em um DataFrame
print(df_medias)    
                                                                                
# Salvar o DataFrame em um arquivo CSV
df_medias.to_csv('Media_Consumo.csv', index=False)

