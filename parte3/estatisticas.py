import pandas as pd
import matplotlib.pyplot as plt

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

# Calcular as estatísticas (média, desvio padrão e variância) para cada taxa por hora para cada dispositivo
stats_smart_tv = data_smart_tv.groupby('hour').agg({'bytes_up': ['mean', 'std', 'var'],
                                                   'bytes_down': ['mean', 'std', 'var']})
stats_chromecast = data_chromecast.groupby('hour').agg({'bytes_up': ['mean', 'std', 'var'],
                                                       'bytes_down': ['mean', 'std', 'var']})

# Gráficos para Smart-TV
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Média, Desvio Padrão e Variância - Upload e Download para Smart-TV
for i, (ax, col) in enumerate(zip(axs.flatten(), stats_smart_tv.columns.levels[0])):
    for stat in stats_smart_tv.columns.levels[1]:
        ax.plot(stats_smart_tv.index, stats_smart_tv[col][stat], label=f'{col} - {stat}')

    ax.set_title(f'Smart-TV - {col} por Hora (Log Scale)')
    ax.set_xlabel('Hora do dia')
    ax.set_ylabel('Valor')
    ax.set_yscale('log')
    ax.legend()

plt.tight_layout()
plt.show()

# Gráficos para Chromecast
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Média, Desvio Padrão e Variância - Upload e Download para Chromecast
for i, (ax, col) in enumerate(zip(axs.flatten(), stats_chromecast.columns.levels[0])):
    for stat in stats_chromecast.columns.levels[1]:
        ax.plot(stats_chromecast.index, stats_chromecast[col][stat], label=f'{col} - {stat}')

    ax.set_title(f'Chromecast - {col} por Hora (Log Scale)')
    ax.set_xlabel('Hora do dia')
    ax.set_ylabel('Valor')
    ax.set_yscale('log')
    ax.legend()

plt.tight_layout()
plt.show()


# Smart-TV - Horário com a maior média da taxa de upload em uma hora
max_upload_hour_smart_tv = stats_smart_tv['bytes_up']['mean'].idxmax()
max_upload_mean_smart_tv = stats_smart_tv['bytes_up']['mean'].max()
print(f"Horário com a maior média da taxa de upload em uma hora, Smart-TV: {max_upload_hour_smart_tv} - Média: {max_upload_mean_smart_tv}")

# Smart-TV - Horário com a maior média da taxa de download em uma hora
max_download_hour_smart_tv = stats_smart_tv['bytes_down']['mean'].idxmax()
max_download_mean_smart_tv = stats_smart_tv['bytes_down']['mean'].max()
print(f"Horário com a maior média da taxa de download em uma hora, Smart-TV: {max_download_hour_smart_tv} - Média: {max_download_mean_smart_tv}")

# Chromecast - Horário com a maior média da taxa de upload em uma hora
max_upload_hour_chromecast = stats_chromecast['bytes_up']['mean'].idxmax()
max_upload_mean_chromecast = stats_chromecast['bytes_up']['mean'].max()
print(f"Horário com a maior média da taxa de upload em uma hora, Chromecast: {max_upload_hour_chromecast} - Média: {max_upload_mean_chromecast}")

# Chromecast - Horário com a maior média da taxa de download em uma hora
max_download_hour_chromecast = stats_chromecast['bytes_down']['mean'].idxmax()
max_download_mean_chromecast = stats_chromecast['bytes_down']['mean'].max()
print(f"Horário com a maior média da taxa de download em uma hora, Chromecast: {max_download_hour_chromecast} - Média: {max_download_mean_chromecast}")

