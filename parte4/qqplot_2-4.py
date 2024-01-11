import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os datasets dos bytes_down
file_dataset2_smart_tv = 'dataset2_smart_tv.csv'
file_dataset4_chromecast = 'dataset4_chromecast.csv'

dataset2_smart_tv = pd.read_csv(file_dataset2_smart_tv)
dataset4_chromecast = pd.read_csv(file_dataset4_chromecast)

# Interpolação linear para igualar o número de linhas dos datasets
num_rows = min(len(dataset2_smart_tv), len(dataset4_chromecast))
dataset2_smart_tv = dataset2_smart_tv.iloc[:num_rows]
dataset4_chromecast = dataset4_chromecast.iloc[:num_rows]
dataset4_chromecast['bytes_down'] = dataset4_chromecast['bytes_down'].interpolate(method='linear')

# Aplicar escala logarítmica aos valores de bytes_down (tratando zeros)
dataset2_smart_tv['log_bytes_down'] = np.log10(dataset2_smart_tv['bytes_down'].replace(0, 1))
dataset4_chromecast['log_bytes_down'] = np.log10(dataset4_chromecast['bytes_down'].replace(0, 1))

# Organizar os dados para o QQ plot
sorted_dataset2 = np.sort(dataset2_smart_tv['log_bytes_down'])
sorted_dataset4 = np.sort(dataset4_chromecast['log_bytes_down'])

# Gerar QQ plot entre as colunas bytes_down dos datasets após a interpolação
plt.figure(figsize=(6, 6))
plt.scatter(sorted_dataset2, sorted_dataset4)
plt.plot(sorted_dataset2, sorted_dataset2, color='red', linestyle='--')  # Linha y = x
plt.title('QQ Plot - bytes_down - Smart-TV vs Chromecast')
plt.xlabel('Quantis Smart-TV (log)')
plt.ylabel('Quantis Chromecast (log)')

plt.tight_layout()
plt.show()
