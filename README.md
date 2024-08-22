# Estimativa de Memória Computacional para Moléculas Utilizando B3LYP/6-31G\*\*

Este repositório contém um script em Python que estima a memória computacional necessária para diferentes moléculas usando dados derivados de cálculos B3LYP/6-31G** realizados no software Orca. O script extrapola os requisitos de memória para moléculas maiores com base em dados conhecidos e plota os resultados comparando as moléculas verificadas e estimadas.

## Recursos

- Estimativa de memória computacional (em MB) por núcleo de processador para moléculas de diferentes tamanhos.
- Comparação entre os dados de memória verificados e os valores estimados para novas moléculas.
- Visualização gráfica das estimativas e dos valores reais, com destaque para as moléculas e seus coeficientes de escala.

## Dependências

O script requer as seguintes bibliotecas Python:

- `numpy`: Para operações numéricas.
- `matplotlib`: Para a criação dos gráficos.

Você pode instalar essas dependências usando o seguinte comando:

```bash
pip install numpy matplotlib
