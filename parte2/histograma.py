import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os datasets

file_smart_tv = 'dataset_smart-tv.csv'
file_chromecast = 'dataset_chromecast.csv'

# Leitura dos datasets

data_smart_tv = pd.read_csv(file_smart_tv)
data_chromecast = pd.read_csv(file_chromecast)

# Selecionar as colunas bytes_up e bytes_down para cada tipo de dispositivo
bytes_up_smart_tv = data_smart_tv['bytes_up']
bytes_up_chromecast = data_chromecast['bytes_up']
bytes_down_smart_tv = data_smart_tv['bytes_down']
bytes_down_chromecast = data_chromecast['bytes_down']

# Adicionar um valor pequeno (ex: 1) para evitar zeros ou negativos
epsilon = 1
bytes_up_smart_tv_log = np.log10(bytes_up_smart_tv + epsilon)
bytes_up_chromecast_log = np.log10(bytes_up_chromecast + epsilon)
bytes_down_smart_tv_log = np.log10(bytes_down_smart_tv + epsilon)
bytes_down_chromecast_log = np.log10(bytes_down_chromecast + epsilon)

# Definir bins de acordo com Sturges, garantindo limites finitos
num_bins_up_smart_tv = int(1 + np.log2(len(bytes_up_smart_tv.dropna())))
num_bins_up_chromecast = int(1 + np.log2(len(bytes_up_chromecast.dropna())))
num_bins_down_smart_tv = int(1 + np.log2(len(bytes_down_smart_tv.dropna())))
num_bins_down_chromecast = int(1 + np.log2(len(bytes_down_chromecast.dropna())))

# Gerar os histogramas com os bins calculados e limites definidos
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Histograma para bytes_up do Chromecast
axs[0, 0].hist(bytes_up_chromecast_log.dropna(), bins=num_bins_up_chromecast, range=(0, 8))
axs[0, 0].set_title('Histograma Bytes Up - Chromecast')
axs[0, 0].set_xlabel('Bytes Up (log scale)')
axs[0, 0].set_ylabel('Frequência')

# Histograma para bytes_down do Chromecast
axs[0, 1].hist(bytes_down_chromecast_log.dropna(), bins=num_bins_down_chromecast, range=(0, 8))
axs[0, 1].set_title('Histograma Bytes Down - Chromecast')
axs[0, 1].set_xlabel('Bytes Down (log scale)')
axs[0, 1].set_ylabel('Frequência')

# Histograma para bytes_up da Smart-TV
axs[1, 0].hist(bytes_up_smart_tv_log.dropna(), bins=num_bins_up_smart_tv, range=(0, 8))
axs[1, 0].set_title('Histograma Bytes Up - Smart-TV')
axs[1, 0].set_xlabel('Bytes Up (log scale)')
axs[1, 0].set_ylabel('Frequência')

# Histograma para bytes_down da Smart-TV
axs[1, 1].hist(bytes_down_smart_tv_log.dropna(), bins=num_bins_down_smart_tv, range=(0, 8))
axs[1, 1].set_title('Histograma Bytes Down - Smart-TV')
axs[1, 1].set_xlabel('Bytes Down (log scale)')
axs[1, 1].set_ylabel('Frequência')

# Ajustar layout
plt.tight_layout()
plt.show()
