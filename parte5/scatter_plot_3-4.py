import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os datasets 1 e 2
file_dataset3_chromecast = 'dataset3_chromecast.csv'
file_dataset4_chromecast = 'dataset4_chromecast.csv'

# Leitura dos datasets
dataset3_chromecast = pd.read_csv(file_dataset3_chromecast)
dataset4_chromecast = pd.read_csv(file_dataset4_chromecast)

# Aplicar escala logarítmica e tratando zeros
dataset3_chromecast['log_bytes_up'] = np.log10(dataset3_chromecast['bytes_up'].replace(0, 1))
dataset4_chromecast['log_bytes_down'] = np.log10(dataset4_chromecast['bytes_down'].replace(0, 1))

# Gerar o scatter plot
plt.scatter(dataset3_chromecast['log_bytes_up'], dataset4_chromecast['log_bytes_down'], color='red', alpha=0.05)
plt.xlabel('Bytes enviados')
plt.ylabel('Bytes recebidos')
plt.title('Chromecast')
plt.show()


