import numpy as np
import matplotlib.pyplot as plt

# --- Estimativa de Memória Molecular com B3LYP/6-31G** ---
# Este script estima a memória computacional necessária para uma série de moléculas
# usando dados derivados de cálculos B3LYP/6-31G** realizados no Orca.
# Ele extrapola os requisitos de memória para moléculas maiores com base em dados conhecidos e plota os resultados.

# --- Dados Conhecidos ---
# Moléculas conhecidas com uso de memória verificado
moleculas_verificadas = ['C$_{24}$H$_{12}$','C$_{54}$H$_{18}$', 'C$_{96}$H$_{24}$', 
                         'C$_{150}$H$_{30}$', 'C$_{216}$H$_{36}$', 'C$_{294}$H$_{42}$', 
                         'C$_{384}$H$_{48}$']
quantidade_carbonos_verificada = np.array([24, 54, 96, 150, 216, 294, 384])
memoria_verificada = np.array([87.3, 223.5, 479.2, 882.1, 1516.5, 2464.7, 3841.8])

# --- Inicialização ---
# Comece com as moléculas para as quais o uso de memória foi verificado
moleculas_estimadas = ['C$_{24}$H$_{12}$','C$_{54}$H$_{18}$', 'C$_{96}$H$_{24}$']
quantidade_carbonos = np.array([24, 54, 96])
memoria_estimada = np.array([87.3, 223.5, 479.2])

# Cores para cada ponto da molécula
cores = ['g', 'c', 'm', 'y', 'k', 'b', 'r']

# --- Cálculo dos Coeficientes de Crescimento ---
# Calcule os coeficientes de escala (memória por átomo de carbono) para as moléculas conhecidas
coeficientes = memoria_estimada / quantidade_carbonos

# Calcule a variação percentual entre os coeficientes de escala consecutivos
variacoes_percentuais = [(y - x) / x for x, y in zip(coeficientes[:-1], coeficientes[1:])]

# --- Loop de Estimativa ---
# Estime iterativamente os coeficientes e a memória para as novas moléculas
for nova_quantidade in [150, 216, 294, 384]:
    # Calcule a última variação percentual conhecida ou calculada
    variacao_percentual = variacoes_percentuais[-1]
    
    # Estime o novo coeficiente de escala
    novo_coeficiente = coeficientes[-1] * (1 + variacao_percentual)
    
    # Estime a memória para a nova molécula
    nova_memoria = novo_coeficiente * nova_quantidade
    
    # Adicione a nova molécula e suas estimativas aos arrays existentes
    quantidade_carbonos = np.append(quantidade_carbonos, nova_quantidade)
    memoria_estimada = np.append(memoria_estimada, nova_memoria)
    moleculas_estimadas.append(f'C$_{{{nova_quantidade}}}$H$_{{{int(np.sqrt(nova_quantidade / 6) * 6)}}}$')  # Ajusta H de acordo com a proporção

    # Atualize os coeficientes e variações percentuais com o novo valor
    coeficientes = np.append(coeficientes, novo_coeficiente)
    variacoes_percentuais.append((novo_coeficiente - coeficientes[-2]) / coeficientes[-2])

# --- Plotando os Resultados ---
plt.figure(figsize=(12, 6))

# Adicione pontos estimados
for i in range(len(quantidade_carbonos)):
    plt.plot(quantidade_carbonos[i], memoria_estimada[i], marker='o', linestyle='None', 
             color=cores[i % len(cores)], label=moleculas_estimadas[i])

# Adicione linha sólida entre os pontos verificados
for i in range(len(quantidade_carbonos) - 5):
    plt.plot([quantidade_carbonos[i], quantidade_carbonos[i+1]], [memoria_estimada[i], memoria_estimada[i+1]], 
             linestyle='-', color='black', label='_nolegend_')

# Adicione linha tracejada entre o último ponto verificado e os pontos estimados
for i in range(len(quantidade_carbonos) - 5, len(quantidade_carbonos) - 1):
    plt.plot([quantidade_carbonos[i], quantidade_carbonos[i+1]], [memoria_estimada[i], memoria_estimada[i+1]], 
             linestyle='--', color='gray', label='_nolegend_')

# Adicione a linha para os valores verificados, começando após os dois primeiros pontos
plt.plot(quantidade_carbonos_verificada[2:], memoria_verificada[2:], linestyle='-', color='blue', 
         label='Verificados')

# Adicione rótulos e título
plt.xlabel('Quantidade de Átomos de Carbono', fontsize=18)
plt.ylabel('Memória por Núcleo (MB)', fontsize=18)
plt.title('B3LYP/6-31G** - Orca', fontsize=18)

# Adicione legenda manualmente para os pontos das moléculas, na horizontal, no centro e acima do gráfico
handles_moleculas = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cores[i % len(cores)], 
                                markersize=6, label=moleculas_estimadas[i]) for i in range(len(moleculas_estimadas))]
first_legend = plt.legend(handles=handles_moleculas, loc='upper center', bbox_to_anchor=(0.65, 0.15), 
                          ncol=4, fontsize=14)
plt.gca().add_artist(first_legend)

# Adicione legenda manualmente para as linhas em outro estilo
handles_linhas = [plt.Line2D([0], [0], linestyle='-', color='black', label='Verificados - base para estimativa'),
                  plt.Line2D([0], [0], linestyle='--', color='gray', label='Estimados'),
                  plt.Line2D([0], [0], linestyle='-', color='blue', label='Verificados')]
plt.legend(handles=handles_linhas, loc='upper left', fontsize=14)

# Adicione valores exatos ao lado dos pontos no eixo y
for i in range(len(quantidade_carbonos)):
    plt.text(quantidade_carbonos[i], memoria_estimada[i], f'{memoria_estimada[i]:.1f}', 
             ha='right', va='bottom', fontsize=16)

# Ajuste o tamanho das etiquetas dos ticks nos eixos x e y
plt.tick_params(axis='x', labelsize=16)
plt.tick_params(axis='y', labelsize=16)

plt.grid(True)
plt.show()

