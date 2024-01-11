import pandas as pd

# Carregar os datasets originais
file_smart_tv = 'dataset_smart-tv.csv'
file_chromecast = 'dataset_chromecast.csv'

# Carregar os dados
data_smart_tv = pd.read_csv(file_smart_tv)
data_chromecast = pd.read_csv(file_chromecast)

# Converter a coluna date_hour para o tipo datetime
data_smart_tv['date_hour'] = pd.to_datetime(data_smart_tv['date_hour'])
data_chromecast['date_hour'] = pd.to_datetime(data_chromecast['date_hour'])

# Extrair a informação da hora
data_smart_tv['hour'] = data_smart_tv['date_hour'].dt.hour
data_chromecast['hour'] = data_chromecast['date_hour'].dt.hour

# Calcular as estatísticas (média, desvio padrão e variância) para cada taxa por hora para cada dispositivo
stats_smart_tv = data_smart_tv.groupby('hour').agg({'bytes_up': ['mean', 'std', 'var'],
                                                   'bytes_down': ['mean', 'std', 'var']})
stats_chromecast = data_chromecast.groupby('hour').agg({'bytes_up': ['mean', 'std', 'var'],
                                                       'bytes_down': ['mean', 'std', 'var']})

# Encontrar os horários com as maiores médias da taxa de upload e download para Smart-TV e Chromecast
max_upload_hour_smart_tv = stats_smart_tv['bytes_up']['mean'].idxmax()
max_download_hour_smart_tv = stats_smart_tv['bytes_down']['mean'].idxmax()
max_upload_hour_chromecast = stats_chromecast['bytes_up']['mean'].idxmax()
max_download_hour_chromecast = stats_chromecast['bytes_down']['mean'].idxmax()

# Filtrar os dados para os horários com as maiores médias da taxa de upload e download para Smart-TV e Chromecast
dataset1_smart_tv = data_smart_tv[data_smart_tv['hour'] == max_upload_hour_smart_tv]
dataset2_smart_tv = data_smart_tv[data_smart_tv['hour'] == max_download_hour_smart_tv]
dataset3_chromecast = data_chromecast[data_chromecast['hour'] == max_upload_hour_chromecast]
dataset4_chromecast = data_chromecast[data_chromecast['hour'] == max_download_hour_chromecast]

# Salvar os datasets filtrados em arquivos separados
dataset1_smart_tv.to_csv('dataset1_smart_tv.csv', index=False)
dataset2_smart_tv.to_csv('dataset2_smart_tv.csv', index=False)
dataset3_chromecast.to_csv('dataset3_chromecast.csv', index=False)
dataset4_chromecast.to_csv('dataset4_chromecast.csv', index=False)
