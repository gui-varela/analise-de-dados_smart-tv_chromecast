import pandas as pd

# Carregar os datasets 1 e 2
file_dataset1_smart_tv = 'dataset1_smart_tv.csv'
file_dataset2_smart_tv = 'dataset2_smart_tv.csv'

# Leitura dos datasets
dataset1_smart_tv = pd.read_csv(file_dataset1_smart_tv)
dataset2_smart_tv = pd.read_csv(file_dataset2_smart_tv)

# Calcular o coeficiente de correlação amostral
correlation_coefficient = dataset1_smart_tv['bytes_up'].corr(dataset2_smart_tv['bytes_down'])

# Exibir o resultado
print(f"[SMART-TV]\nCoeficiente de correlação amostral entre bytes_up e bytes_down: {correlation_coefficient}")

# Carregar os datasets 3 e 4
file_dataset3_chromecast = 'dataset3_chromecast.csv'
file_dataset4_chromecast = 'dataset4_chromecast.csv'

# Leitura dos datasets
dataset3_chromecast = pd.read_csv(file_dataset3_chromecast)
dataset4_chromecast = pd.read_csv(file_dataset4_chromecast)

# Calcular o coeficiente de correlação amostral
correlation_coefficient = dataset3_chromecast['bytes_up'].corr(dataset4_chromecast['bytes_down'])

# Exibir o resultado
print(f"\n[CHROMECAST]\nCoeficiente de correlação amostral entre bytes_up e bytes_down: {correlation_coefficient}")