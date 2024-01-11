import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os datasets após a interpolação
file_dataset1_smart_tv = 'dataset1_smart_tv.csv'
file_dataset3_chromecast = 'dataset3_chromecast.csv'

dataset1_smart_tv = pd.read_csv(file_dataset1_smart_tv)
dataset3_chromecast = pd.read_csv(file_dataset3_chromecast)

# Interpolação linear para igualar o número de linhas dos datasets
num_rows = min(len(dataset1_smart_tv), len(dataset3_chromecast))
dataset1_smart_tv = dataset1_smart_tv.iloc[:num_rows]
dataset3_chromecast = dataset3_chromecast.iloc[:num_rows]
dataset3_chromecast['bytes_up'] = dataset3_chromecast['bytes_up'].interpolate(method='linear')

# Aplicar escala logarítmica aos valores de bytes_up (tratando zeros)
dataset1_smart_tv['log_bytes_up'] = np.log10(dataset1_smart_tv['bytes_up'].replace(0, 1))
dataset3_chromecast['log_bytes_up'] = np.log10(dataset3_chromecast['bytes_up'].replace(0, 1))

# Organizar os dados para o QQ plot
sorted_dataset1 = np.sort(dataset1_smart_tv['log_bytes_up'])
sorted_dataset3 = np.sort(dataset3_chromecast['log_bytes_up'])

# Gerar QQ plot entre as colunas bytes_up dos datasets após a interpolação
plt.figure(figsize=(6, 6))
plt.scatter(sorted_dataset1, sorted_dataset3)
plt.plot(sorted_dataset1, sorted_dataset1, color='red', linestyle='--')  # Linha y = x
plt.title('QQ Plot - bytes_up - Smart-TV vs Chromecast')
plt.xlabel('Quantis Smart-TV (log)')
plt.ylabel('Quantis Chromecast (log)')

plt.tight_layout()
plt.show()
