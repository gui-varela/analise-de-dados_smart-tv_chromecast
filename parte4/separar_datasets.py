import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# Carregar os datasets filtrados
file_dataset1_smart_tv = 'dataset1_smart_tv.csv'
file_dataset2_smart_tv = 'dataset2_smart_tv.csv'
file_dataset3_chromecast = 'dataset3_chromecast.csv'
file_dataset4_chromecast = 'dataset4_chromecast.csv'

# Carregar os dados
dataset1_smart_tv = pd.read_csv(file_dataset1_smart_tv)
dataset2_smart_tv = pd.read_csv(file_dataset2_smart_tv)
dataset3_chromecast = pd.read_csv(file_dataset3_chromecast)
dataset4_chromecast = pd.read_csv(file_dataset4_chromecast)

# Ordenar os datasets
sorted_dataset1_smart_tv = np.sort(dataset1_smart_tv['bytes_up'])
sorted_dataset2_smart_tv = np.sort(dataset2_smart_tv['bytes_down'])
sorted_dataset3_chromecast = np.sort(dataset3_chromecast['bytes_up'])
sorted_dataset4_chromecast = np.sort(dataset4_chromecast['bytes_down'])

# Calcular os quantis para os datasets menores
quantiles_dataset3_chromecast = np.arange(0, len(sorted_dataset3_chromecast)) / (len(sorted_dataset1_smart_tv) - 1)
quantiles_dataset4_chromecast = np.arange(0, len(sorted_dataset4_chromecast)) / (len(sorted_dataset2_smart_tv) - 1)

# Interpolação linear para encontrar os pontos correspondentes nos quantis dos datasets maiores
interp_func_1 = interp1d(quantiles_dataset3_chromecast, sorted_dataset3_chromecast, bounds_error=False)
interp_values_dataset1_smart_tv = interp_func_1(np.arange(0, len(sorted_dataset1_smart_tv)) / (len(sorted_dataset1_smart_tv) - 1))

interp_func_2 = interp1d(quantiles_dataset4_chromecast, sorted_dataset4_chromecast, bounds_error=False)
interp_values_dataset2_smart_tv = interp_func_2(np.arange(0, len(sorted_dataset2_smart_tv)) / (len(sorted_dataset2_smart_tv) - 1))

# Criar novos datasets alinhados com a interpolação
new_dataset1 = pd.DataFrame({'bytes_up': interp_values_dataset1_smart_tv})
new_dataset2 = pd.DataFrame({'bytes_down': interp_values_dataset2_smart_tv})

# Salvar os novos datasets
new_dataset1.to_csv('new_dataset1.csv', index=False)
new_dataset2.to_csv('new_dataset2.csv', index=False)
