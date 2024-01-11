import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os datasets 1 e 2
file_dataset1_smart_tv = 'dataset1_smart_tv.csv'
file_dataset2_smart_tv = 'dataset2_smart_tv.csv'

# Leitura dos datasets
dataset1_smart_tv = pd.read_csv(file_dataset1_smart_tv)
dataset2_smart_tv = pd.read_csv(file_dataset2_smart_tv)

# Interpolação linear para igualar o número de linhas dos datasets
num_rows = min(len(dataset1_smart_tv), len(dataset2_smart_tv))
dataset1_smart_tv = dataset1_smart_tv.iloc[:num_rows]
dataset2_smart_tv = dataset2_smart_tv.iloc[:num_rows]
dataset2_smart_tv['bytes_down'] = dataset2_smart_tv['bytes_down'].interpolate(method='linear')

# Aplicar escala logarítmica e tratando zeros
dataset1_smart_tv['log_bytes_up'] = np.log10(dataset1_smart_tv['bytes_up'].replace(0, 1))
dataset2_smart_tv['log_bytes_down'] = np.log10(dataset2_smart_tv['bytes_down'].replace(0, 1))

# Gerar o scatter plot
plt.scatter(dataset1_smart_tv['log_bytes_up'], dataset2_smart_tv['log_bytes_down'], color='blue', alpha=0.02)
plt.xlabel('Bytes enviados')
plt.ylabel('Bytes recebidos')
plt.title('Smart_TV')
plt.show()
