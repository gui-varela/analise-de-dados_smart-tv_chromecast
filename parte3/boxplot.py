import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Aplicar a escala logarítmica aos dados
data_smart_tv['log_bytes_up'] = np.log10(data_smart_tv['bytes_up'].replace(0, 1))
data_smart_tv['log_bytes_down'] = np.log10(data_smart_tv['bytes_down'].replace(0, 1))
data_chromecast['log_bytes_up'] = np.log10(data_chromecast['bytes_up'].replace(0, 1))
data_chromecast['log_bytes_down'] = np.log10(data_chromecast['bytes_down'].replace(0, 1))

# Criar os gráficos de boxplot para cada dispositivo e suas taxas de download/upload por hora
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Boxplots para Smart-TV - Upload
data_smart_tv.boxplot(column='log_bytes_up', by='hour', ax=axs[0, 0])
axs[0, 0].set_title('Smart-TV - Bytes Up por Hora (Log Scale)')
axs[0, 0].set_xlabel('Hora do dia')
axs[0, 0].set_ylabel('Bytes Up (log scale)')

# Boxplots para Smart-TV - Download
data_smart_tv.boxplot(column='log_bytes_down', by='hour', ax=axs[0, 1])
axs[0, 1].set_title('Smart-TV - Bytes Down por Hora (Log Scale)')
axs[0, 1].set_xlabel('Hora do dia')
axs[0, 1].set_ylabel('Bytes Down (log scale)')

# Boxplots para Chromecast - Upload
data_chromecast.boxplot(column='log_bytes_up', by='hour', ax=axs[1, 0])
axs[1, 0].set_title('Chromecast - Bytes Up por Hora (Log Scale)')
axs[1, 0].set_xlabel('Hora do dia')
axs[1, 0].set_ylabel('Bytes Up (log scale)')

# Boxplots para Chromecast - Download
data_chromecast.boxplot(column='log_bytes_down', by='hour', ax=axs[1, 1])
axs[1, 1].set_title('Chromecast - Bytes Down por Hora (Log Scale)')
axs[1, 1].set_xlabel('Hora do dia')
axs[1, 1].set_ylabel('Bytes Down (log scale)')

# Ajustar layout
plt.tight_layout()
plt.show()
