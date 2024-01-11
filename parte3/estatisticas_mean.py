import pandas as pd
import matplotlib.pyplot as plt

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

# Calcular a média para cada taxa por hora para cada dispositivo
mean_smart_tv = data_smart_tv.groupby('hour').mean()
mean_chromecast = data_chromecast.groupby('hour').mean()

# Gráficos de média para Smart-TV e Chromecast
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Média - Download Smart-TV
axs[0, 0].plot(mean_smart_tv.index, mean_smart_tv['bytes_down'], label='Smart-TV - Download (Média)')
axs[0, 0].set_title('Média do Download para Smart-TV')
axs[0, 0].set_xlabel('Hora do dia')
axs[0, 0].set_ylabel('Média')
axs[0, 0].set_yscale('log')
axs[0, 0].legend()

# Média - Upload Smart-TV
axs[0, 1].plot(mean_smart_tv.index, mean_smart_tv['bytes_up'], label='Smart-TV - Upload (Média)')
axs[0, 1].set_title('Média do Upload para Smart-TV')
axs[0, 1].set_xlabel('Hora do dia')
axs[0, 1].set_ylabel('Média')
axs[0, 1].set_yscale('log')
axs[0, 1].legend()

# Média - Download Chromecast
axs[1, 0].plot(mean_chromecast.index, mean_chromecast['bytes_down'], label='Chromecast - Download (Média)')
axs[1, 0].set_title('Média do Download para Chromecast')
axs[1, 0].set_xlabel('Hora do dia')
axs[1, 0].set_ylabel('Média')
axs[1, 0].set_yscale('log')
axs[1, 0].legend()

# Média - Upload Chromecast
axs[1, 1].plot(mean_chromecast.index, mean_chromecast['bytes_up'], label='Chromecast - Upload (Média)')
axs[1, 1].set_title('Média do Upload para Chromecast')
axs[1, 1].set_xlabel('Hora do dia')
axs[1, 1].set_ylabel('Média')
axs[1, 1].set_yscale('log')
axs[1, 1].legend()

plt.tight_layout()
plt.show()
