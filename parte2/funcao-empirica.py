import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

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

# Adicionar um valor pequeno (ex: 1e-10) para evitar zeros ao calcular o logaritmo
epsilon = 1e-10
bytes_up_smart_tv_log = np.log10(bytes_up_smart_tv + epsilon)
bytes_up_chromecast_log = np.log10(bytes_up_chromecast + epsilon)
bytes_down_smart_tv_log = np.log10(bytes_down_smart_tv + epsilon)
bytes_down_chromecast_log = np.log10(bytes_down_chromecast + epsilon)

# Criar as funções de distribuição empírica (ECDF)
ecdf_bytes_up_chromecast = sm.distributions.ECDF(bytes_up_chromecast_log)
ecdf_bytes_down_chromecast = sm.distributions.ECDF(bytes_down_chromecast_log)
ecdf_bytes_up_smart_tv = sm.distributions.ECDF(bytes_up_smart_tv_log)
ecdf_bytes_down_smart_tv = sm.distributions.ECDF(bytes_down_smart_tv_log)

# Gerar o plot das ECDFs
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Definir os limites do eixo x em escala logarítmica
x_limits = [0, 8]

# ECDF para bytes_up do Chromecast
x_bytes_up_chromecast = np.linspace(x_limits[0], x_limits[1], len(bytes_up_chromecast_log))
y_bytes_up_chromecast = ecdf_bytes_up_chromecast(x_bytes_up_chromecast)
axs[0, 0].plot(x_bytes_up_chromecast, y_bytes_up_chromecast)
axs[0, 0].set_title('ECDF Bytes Up - Chromecast')
axs[0, 0].set_xlabel('Bytes Up (log scale)')
axs[0, 0].set_ylabel('ECDF')
axs[0, 0].set_xlim(x_limits)

# ECDF para bytes_down do Chromecast
x_bytes_down_chromecast = np.linspace(x_limits[0], x_limits[1], len(bytes_down_chromecast_log))
y_bytes_down_chromecast = ecdf_bytes_down_chromecast(x_bytes_down_chromecast)
axs[0, 1].plot(x_bytes_down_chromecast, y_bytes_down_chromecast)
axs[0, 1].set_title('ECDF Bytes Down - Chromecast')
axs[0, 1].set_xlabel('Bytes Down (log scale)')
axs[0, 1].set_ylabel('ECDF')
axs[0, 1].set_xlim(x_limits)

# ECDF para bytes_up da Smart-TV
x_bytes_up_smart_tv = np.linspace(x_limits[0], x_limits[1], len(bytes_up_smart_tv_log))
y_bytes_up_smart_tv = ecdf_bytes_up_smart_tv(x_bytes_up_smart_tv)
axs[1, 0].plot(x_bytes_up_smart_tv, y_bytes_up_smart_tv)
axs[1, 0].set_title('ECDF Bytes Up - Smart-TV')
axs[1, 0].set_xlabel('Bytes Up (log scale)')
axs[1, 0].set_ylabel('ECDF')
axs[1, 0].set_xlim(x_limits)

# ECDF para bytes_down da Smart-TV
x_bytes_down_smart_tv = np.linspace(x_limits[0], x_limits[1], len(bytes_down_smart_tv_log))
y_bytes_down_smart_tv = ecdf_bytes_down_smart_tv(x_bytes_down_smart_tv)
axs[1, 1].plot(x_bytes_down_smart_tv, y_bytes_down_smart_tv)
axs[1, 1].set_title('ECDF Bytes Down - Smart-TV')
axs[1, 1].set_xlabel('Bytes Down (log scale)')
axs[1, 1].set_ylabel('ECDF')
axs[1, 1].set_xlim(x_limits)

# Ajustar layout
plt.tight_layout()
plt.show()
