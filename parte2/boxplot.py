import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os datasets

file_smart_tv = 'dataset_smart-tv.csv'
file_chromecast = 'dataset_chromecast.csv'

# Leitura dos datasets

data_smart_tv = pd.read_csv(file_smart_tv)
data_chromecast = pd.read_csv(file_chromecast)

# Adicionar um valor pequeno (1e-10) aos zeros nos dados antes de aplicar a transformação logarítmica
data_smart_tv['log_bytes_up'] = np.log10(data_smart_tv['bytes_up'].replace(0, 1e-10))
data_smart_tv['log_bytes_down'] = np.log10(data_smart_tv['bytes_down'].replace(0, 1e-10))
data_chromecast['log_bytes_up'] = np.log10(data_chromecast['bytes_up'].replace(0, 1e-10))
data_chromecast['log_bytes_down'] = np.log10(data_chromecast['bytes_down'].replace(0, 1e-10))

# Selecionar os dados transformados
bytes_up_smart_tv = data_smart_tv['log_bytes_up']
bytes_up_chromecast = data_chromecast['log_bytes_up']
bytes_down_smart_tv = data_smart_tv['log_bytes_down']
bytes_down_chromecast = data_chromecast['log_bytes_down']

# Criar um boxplot comparando bytes_up e bytes_down entre Smart-TV e Chromecast
plt.figure(figsize=(8, 6))

# Configurações visuais para os boxplots de bytes_up e bytes_down
boxplot = plt.boxplot([bytes_up_smart_tv, bytes_up_chromecast, bytes_down_smart_tv, bytes_down_chromecast],
                      positions=[1, 2, 4, 5], labels=['Smart-TV (Up)', 'Chromecast (Up)', 'Smart-TV (Down)', 'Chromecast (Down)'],
                      widths=0.5, patch_artist=True)

# Colorir os boxplots
colors = ['lightblue', 'lightgreen', 'yellow', 'lightsalmon']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

plt.ylim(0, 9)  # Definir intervalo do eixo y entre 0 e 8 (escala logarítmica)
plt.title('Comparação de Bytes Up/Down entre Smart-TV e Chromecast (Escala Logarítmica)')
plt.ylabel('Bytes (log scale)')
plt.legend(['Bytes Up (Smart-TV)', 'Bytes Up (Chromecast)', 'Bytes Down (Smart-TV)', 'Bytes Down (Chromecast)'])
plt.show()
