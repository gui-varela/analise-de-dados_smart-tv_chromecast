# Instruções de execução

- Os códigos usados para construir este relatório estão disponíveis neste link do Drive ou neste link do Github
- O código está organizado em pastas (parte2, parte3, …, parte5) referentes às seções deste relatório. Por exemplo, a pasta “parte2” é dedicada a gerar os gráficos e estatísticas da seção 2 do relatório (2. Estatísticas gerais, pág. 3)
- Antes de executar em um editor de código, é necessário descompactar os datasets principais na mesma pasta, que estão compactados devido ao extenso tamanho destes
- Feito isso, basta entrar em cada pasta e executar manualmente o arquivo desejado. Por exemplo, para gerar o gráfico da figura 9, é preciso acessar parte5/scatter_plot_1-2.py

# Explicação do código

Na pasta raiz, além das pastas onde estão os códigos para geração de gráficos e estatísticas, há 7 arquivos:

  1. Os arquivos .zip são os datasets originais, que devem ser descompactados antes da execução dos códigos
  2. O arquivo gerar_novos_datasets.py é o arquivo que gera os novos datasets que são utilizados nas seções 4 e 4
  3. Os arquivos .csv são os datasets gerados pelo gerar_novos_datasets.py

Todos os arquivos estão comentados com o passo a passo da execução do código. Para executar estratégias como transformar os dados para escala logarítmica e fazer interpolação para ajustar os quantis aos datasets de tamanhos diferentes, além da geração de gráficos e estatísticas, foram usadas funções auxiliares das bibliotecas Pandas, Matplotlib e Numpy.
