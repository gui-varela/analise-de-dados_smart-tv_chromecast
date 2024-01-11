import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os 4 datasets filtrados
file_dataset1_smart_tv = 'dataset1_smart_tv.csv'
file_dataset2_smart_tv = 'dataset2_smart_tv.csv'
file_dataset3_chromecast = 'dataset3_chromecast.csv'
file_dataset4_chromecast = 'dataset4_chromecast.csv'

# Carregar os dados
dataset1_smart_tv = pd.read_csv(file_dataset1_smart_tv)
dataset2_smart_tv = pd.read_csv(file_dataset2_smart_tv)
dataset3_chromecast = pd.read_csv(file_dataset3_chromecast)
dataset4_chromecast = pd.read_csv(file_dataset4_chromecast)

# Função para transformar os dados para escala logarítmica, tratando os zeros
def transform_to_log(data):
    return np.log10(data.replace(0, 1))  # Substituir os zeros por 1 para evitar problemas ao calcular o logaritmo

# Aplicar a transformação logarítmica nos dados de upload e download de cada dataset
dataset1_smart_tv['bytes_up'] = transform_to_log(dataset1_smart_tv['bytes_up'])
dataset1_smart_tv['bytes_down'] = transform_to_log(dataset1_smart_tv['bytes_down'])

dataset2_smart_tv['bytes_up'] = transform_to_log(dataset2_smart_tv['bytes_up'])
dataset2_smart_tv['bytes_down'] = transform_to_log(dataset2_smart_tv['bytes_down'])

dataset3_chromecast['bytes_up'] = transform_to_log(dataset3_chromecast['bytes_up'])
dataset3_chromecast['bytes_down'] = transform_to_log(dataset3_chromecast['bytes_down'])

dataset4_chromecast['bytes_up'] = transform_to_log(dataset4_chromecast['bytes_up'])
dataset4_chromecast['bytes_down'] = transform_to_log(dataset4_chromecast['bytes_down'])

# Criar os histogramas para cada dataset
plt.figure(figsize=(10, 8))

plt.subplot(221)
plt.hist(dataset1_smart_tv['bytes_up'], bins='sturges', edgecolor='black')
plt.title('Dataset 1 - Smart-TV Upload (Log Scale)')
plt.xlabel('Bytes Up (Log)')
plt.ylabel('Frequência')

plt.subplot(222)
plt.hist(dataset2_smart_tv['bytes_down'], bins='sturges', edgecolor='black')
plt.title('Dataset 2 - Smart-TV Download (Log Scale)')
plt.xlabel('Bytes Down (Log)')
plt.ylabel('Frequência')

plt.subplot(223)
plt.hist(dataset3_chromecast['bytes_up'], bins='sturges', edgecolor='black')
plt.title('Dataset 3 - Chromecast Upload (Log Scale)')
plt.xlabel('Bytes Up (Log)')
plt.ylabel('Frequência')

plt.subplot(224)
plt.hist(dataset4_chromecast['bytes_down'], bins='sturges', edgecolor='black')
plt.title('Dataset 4 - Chromecast Download (Log Scale)')
plt.xlabel('Bytes Down (Log)')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()
