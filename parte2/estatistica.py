import pandas as pd

# Carregar os datasets
file_smart_tv = 'dataset_smart-tv.csv'
file_chromecast = 'dataset_chromecast.csv'

# Leitura dos datasets
data_smart_tv = pd.read_csv(file_smart_tv)
data_chromecast = pd.read_csv(file_chromecast)

# Calcular estatísticas para cada tipo de dispositivo e cada direção (upload e download)
stats_smart_tv = {
    'Bytes Up': {
        'Média': round(data_smart_tv['bytes_up'].mean(), 1),
        'Variância': round(data_smart_tv['bytes_up'].var(), 1),
        'Desvio Padrão': round(data_smart_tv['bytes_up'].std(), 1)
    },
    'Bytes Down': {
        'Média': round(data_smart_tv['bytes_down'].mean(), 1),
        'Variância': round(data_smart_tv['bytes_down'].var(), 1),
        'Desvio Padrão': round(data_smart_tv['bytes_down'].std(), 1)
    }
}

stats_chromecast = {
    'Bytes Up': {
        'Média': round(data_chromecast['bytes_up'].mean(), 1),
        'Variância': round(data_chromecast['bytes_up'].var(), 1),
        'Desvio Padrão': round(data_chromecast['bytes_up'].std(), 1)
    },
    'Bytes Down': {
        'Média': round(data_chromecast['bytes_down'].mean(), 1),
        'Variância': round(data_chromecast['bytes_down'].var(), 1),
        'Desvio Padrão': round(data_chromecast['bytes_down'].std(), 1)
    }
}

# Mostrar estatísticas para cada dispositivo
print("Estatísticas para Smart-TV:")
print(pd.DataFrame(stats_smart_tv))

print("\nEstatísticas para Chromecast:")
print(pd.DataFrame(stats_chromecast))
